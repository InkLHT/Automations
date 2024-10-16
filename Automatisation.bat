@echo off
rem Les commentaires doivent être sur une seule ligne !
rem Change l'encodage du terminal à UTF-8
chcp 65001 >nul  
echo Démarrage de la surveillance...
start /B python C:\Users\Manel\OneDrive\Bureau\Automatisation\Scripts_Python\Surveillance-docs.py
echo Surveillance démarrée.
pause