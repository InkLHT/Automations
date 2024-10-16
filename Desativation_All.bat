@echo off
rem Change l'encodage du terminal à UTF-8
chcp 65001 >nul
echo Désactivation de tous les scripts Python en cours d'exécution...

REM Tuer tous les scripts Python
taskkill /F /IM python.exe

REM Vérifier si la commande taskkill a fonctionné
if %errorlevel% equ 0 (
    echo Tous les scripts Python ont été désactivés avec succès.
) else (
    echo Une erreur est survenue lors de la désactivation des scripts Python.
    echo Aucun script Python n'était en cours d'exécution ou une autre erreur a eu lieu.
)

pause
