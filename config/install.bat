@echo off
echo Vérification de l'installation de Python...

:: Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Téléchargement et installation de Python...
    :: Télécharge et installe Python
    start /wait https://www.python.org/ftp/python/3.9.9/python-3.9.9.exe /quiet InstallAllUsers=1 PrependPath=1
) else (
    echo Python est déjà installé.
)

:: Vérifier si pip est installé
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo pip n'est pas installé. Installation de pip...
    python -m ensurepip --upgrade
) else (
    echo pip est déjà installé.
)

:: Vérifier si requirements.txt existe
if exist requirements.txt (
    echo Installation des dépendances à partir de requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt non trouvé. Veuillez vous assurer que le fichier est présent dans le répertoire courant.
)

echo Installation terminée.
pause
