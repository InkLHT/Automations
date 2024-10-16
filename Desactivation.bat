@echo off
rem Change l'encodage du terminal à UTF-8
chcp 65001 >nul
echo Désactivation de l'automatisation car je ne sais faire que ça...

rem Lire le PID du fichier dans le dossier logs
set /p PID=<C:\Users\Manel\OneDrive\Bureau\Automatisation\Logs_PID\Surveillance-docs.txt

rem Tuer le processus en utilisant le PID
taskkill /F /PID %PID%

echo Automatisation désactivée ma p'tite vieille.
pause
