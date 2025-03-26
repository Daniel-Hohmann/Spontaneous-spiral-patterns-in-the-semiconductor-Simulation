import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter
import pandas as pd

# ████████ Simulation Parameters █████████
GRID_SIZE = 200        # Entspricht 200μm Probengröße
TIME_STEPS = 500       # Simulationsschritte
DX = 2e-6              # 2μm pro Gitterpunkt (angepasst)
DT = 0.1               # Zeitschritt (wird dynamisch angepasst)

# Materialeigenschaften
DIFFUSION_COEFF = 2e-9 # [m²/s] (reduziert)
ETCH_RATE = 0.15       # Ätzrate 
STRESS_COEFF = 0.15    # Mechanische Kopplung (reduziert)
NOISE_LEVEL = 0.05     # Oberflächenrauheit

# ████████ Hilfsfunktionen █████████
def stabilize(arr):
    arr = np.nan_to_num(arr)
    return np.clip(arr, -1e100, 1e100).astype(np.float64)

def print_stats():
    print(f"Stress: {stress.min():.2f} - {stress.max():.2f}")
    print(f"Concentration: {concentration.min():.2f} - {concentration.max():.2f}")
    print(f"Surface: {surface.min():.2f} - {surface.max():.2f}")

# ████████ Initialisierungen █████████
def create_metal_layer():
    base = np.random.normal(0, 0.1, (GRID_SIZE, GRID_SIZE))
    return gaussian_filter(base, sigma=2) + NOISE_LEVEL * np.random.randn(*base.shape)

# Initiale Bedingungen
surface = create_metal_layer().astype(np.float64)
concentration = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.float64)
stress = np.zeros_like(surface, dtype=np.float64)

# Startbedingung: Zentraler Tropfen
concentration[GRID_SIZE//2-15:GRID_SIZE//2+15, 
             GRID_SIZE//2-15:GRID_SIZE//2+15] = 1.0

# ████████ Physikalische Kernprozesse █████████
def diffusion():
    global concentration, DT
    kernel = np.array([[0.05, 0.2, 0.05],
                       [0.2, -1.0, 0.2],
                       [0.05, 0.2, 0.05]])
    delta = DT * convolve2d(concentration, kernel, 
                            mode='same', boundary='wrap') * DIFFUSION_COEFF/(DX**2 + 1e-12)
    concentration = stabilize(concentration + delta)
    
    # Adaptive Zeitschrittsteuerung
    max_delta = np.max(np.abs(concentration))
    DT = 0.1 if max_delta < 1e3 else 0.01

def mechanical_stress():
    global stress, surface
    stress_kernel = np.array([[0, 1, 0],
                              [1, -4, 1],
                              [0, 1, 0]])
    new_stress = convolve2d(stress, stress_kernel, mode='same', boundary='wrap')
    stress = stabilize(STRESS_COEFF * (new_stress + 0.1 * surface**3))

def etching_process():
    global surface, concentration, stress
    np.clip(stress, -1e3, 1e3, out=stress)
    np.clip(concentration, 0, 1e3, out=concentration)
    
    etch_rate = ETCH_RATE * concentration * (1 + 0.5 * stress)
    surface -= DT * etch_rate
    surface = stabilize(surface)

# ████████ Visualisierung & Analyse █████████
def init_plot():
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    img = ax.imshow(surface, cmap='twilight_shifted', 
                   vmin=-0.5, vmax=0.5, 
                   interpolation='bicubic')
    fig.colorbar(img, label='Surface Deformation [nm]')
    return fig, img

def update_frame(frame):
    diffusion()
    mechanical_stress()
    etching_process()
    
    if frame % 100 == 0:
        print(f"Frame {frame}")
        print_stats()
    
    img.set_array(surface)
    img.set_clim(vmin=surface.min(), vmax=surface.max())
    return img,

# ████████ Hauptsimulation █████████
if __name__ == "__main__":
    print("Starting spiral pattern simulation...")
    print(f"Grid resolution: {GRID_SIZE}x{GRID_SIZE}")
    print(f"Physical scale: {GRID_SIZE*DX*1e6:.0f}μm")
    
    # Setup Animation
    fig, img = init_plot()
    ani = FuncAnimation(fig, update_frame, frames=TIME_STEPS,
                       interval=50, blit=True)
    
    # Datenprotokollierung
    log_data = pd.DataFrame(columns=['Time', 'MaxStress', 'MinHeight'])
    
    plt.show()
    
    # Manuelles Stoppen der Animation
    ani.event_source.stop()
    plt.close(fig)
    
    # Nach Simulation: Daten speichern
    log_data.to_csv('spiral_simulation_log.csv', index=False)
