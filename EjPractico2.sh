#!/bin/bash

mkdir TP2-IDS
cd TP2-IDS
touch app.py 
mkdir static templates
cd static
mkdir css images
cd ..
python3 -m venv .venv

source .venv/bin/activate
pip install flask