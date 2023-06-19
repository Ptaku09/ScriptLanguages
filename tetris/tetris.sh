#!/bin/bash

# Pobierz ścieżkę do skryptu
script_path="$(dirname "$(realpath "$0")")"

# Sprawdź, czy Python jest zainstalowany
if ! command -v python &> /dev/null; then
    echo "Python nie jest zainstalowany. Instalowanie Pythona..."
    sudo apt-get install python -y
fi

# Sprawdź, czy pip jest zainstalowany
if ! command -v pip &> /dev/null; then
    echo "Pip nie jest zainstalowany. Instalowanie pip..."
    sudo apt-get install python-pip -y
fi

# Instalowanie wymaganych bibliotek Pythona
echo "Instalowanie wymaganych bibliotek Pythona..."
pip install sqlalchemy
pip install pygame

python "$script_path/main.py"