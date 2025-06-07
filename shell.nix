# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.gcc
    pkgs.python312
    pkgs.python312Packages.numpy
    pkgs.python312Packages.matplotlib
  ];
}

