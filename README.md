# Spontane Spiralmuster in Halbleitern - Simulation

## Current Issue
nach dem schliesen der simulation die ergebnisse in der .json datei speichern

## Überblick

Dieses Projekt simuliert die Entstehung spontaner Spiralmuster in Halbleitermaterialien, basierend auf dem Experiment, das in [diesem Artikel von Scinexx](https://www.scinexx.de/news/physik/spontane-spiralmuster-im-halbleiter/) beschrieben wird. Die Simulation modelliert die komplexe Interaktion zwischen chemischem Ätzen, mechanischem Stress und Diffusionsprozessen in einer dünnen Metallschicht auf einem Halbleitersubstrat.

## Wissenschaftlicher Hintergrund

Forscher der Technischen Universität Dänemark entdeckten, dass sich beim Ätzen einer dünnen Metallschicht auf Germanium spontan Spiralmuster bilden können. Diese Muster entstehen durch das Zusammenspiel von:

1. Chemischem Ätzen durch eine DNA-haltige Lösung
2. Mechanischem Stress in der Metallschicht
3. Diffusionsprozessen der Ätzlösung

Unsere Simulation versucht, diese Phänomene nachzubilden und zu visualisieren.

## Installation

### Voraussetzungen

- Python 3.7+
- pip (Python Package Installer)

### Schritte

1. Klonen Sie das Repository:
```
git clone https://github.com/Daniel-Hohmann/Spontaneous-spiral-patterns-in-the-semiconductor-Simulation.git
cd Spontaneous-spiral-patterns-in-the-semiconductor-Simulation
```
2. Erstellen Sie eine virtuelle Umgebung (optional, aber empfohlen):
```
python3 -m venv venv
source venv/bin/activate
```
3. Installieren Sie die erforderlichen Pakete:
```
pip install -r requirements.txt
```

## Verwendung

Um die Simulation zu starten, führen Sie einfach das Hauptskript aus:

```
python3 simulation.py
```

Die Simulation wird gestartet und ein Matplotlib-Fenster öffnet sich, das die Entwicklung der Spiralmuster in Echtzeit zeigt.

## Anpassung der Parameter

Sie können verschiedene Parameter in der `simulation.py`-Datei anpassen, um unterschiedliche Szenarien zu simulieren:

- `GRID_SIZE`: Größe des Simulationsgitters
- `TIME_STEPS`: Anzahl der Simulationsschritte
- `DIFFUSION_COEFF`: Diffusionskoeffizient
- `ETCH_RATE`: Ätzrate
- `STRESS_COEFF`: Koeffizient für mechanischen Stress

## Datenanalyse

Nach dem Lauf der Simulation wird eine CSV-Datei `spiral_simulation_log.csv` erstellt, die Daten wie maximalen Stress und minimale Höhe für jeden Zeitschritt enthält. Diese Daten können für weitere Analysen verwendet werden.

## Visualisierung

Die Simulation erzeugt eine farbcodierte Darstellung der Oberflächendeformation. Die Farbskala reicht von blau (Vertiefungen) über grün (neutrale Bereiche) bis rot (Erhebungen).

## Erweiterung
Zu gegebener Zeit möchte ich das Projekt um einige Funktionen erweitern (Parameterstudien, Quantifizierung der Spiralarme, 3D-Visualisierung) und das gesamte Projekt als interaktive Webseite mit Py-Script zur Verfügung stellen.

## 📚 Weiterführende Literatur

- [Originalartikel auf Scinexx](https://www.scinexx.de/news/physik/spontane-spiralmuster-im-halbleiter/)
- [Reaktions-Diffusions-Systeme in der Physik](https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system)
