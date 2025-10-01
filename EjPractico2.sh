#!/bin/bash
set -e #Corta si algo falla

ROOT="TP2-IDS"
VENV_DIR="$ROOT/.venv"

mkdir -p "$ROOT/static/css" "$ROOT/static/images" "$ROOT/templates"
touch "$ROOT/app.py"
python3 -m venv "$VENV_DIR"
