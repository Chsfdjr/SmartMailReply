#!/bin/bash

# Vérifier si Python est installé
if command -v python3 &>/dev/null; then
    echo "Python est déjà installé."
else
    echo "Python n'est pas installé. Installation de Python 3..."
    sudo apt update
    sudo apt install python3 python3-pip -y
fi

# Vérifier si pip est installé
if command -v pip3 &>/dev/null; then
    echo "pip est déjà installé."
else
    echo "pip n'est pas installé. Installation de pip..."
    sudo apt install python3-pip -y
fi

# Vérifier si requirements.txt existe
if [ -f "requirements.txt" ]; then
    echo "Installation des dépendances à partir de requirements.txt..."
    pip3 install -r requirements.txt
else
    echo "requirements.txt non trouvé. Veuillez vous assurer que le fichier est présent dans le répertoire courant."
fi

echo "Installation terminée."
