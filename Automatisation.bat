@echo off
rem Change l'encodage du terminal à UTF-8
chcp 65001 >nul  
echo Démarrage de la surveillance...
start /B python C:\Users\CHEMIN_VERS\VOTRE_SCRIPT
echo Surveillance démarrée.
pause
