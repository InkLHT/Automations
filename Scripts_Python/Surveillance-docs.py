# -*- coding: utf-8 -*-
import os
import shutil
import time
from tqdm import tqdm  # Barre de progression
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Chemins des dossiers
DOSSIER_A_SURVEILLER = r"C:\Users\Manel\OneDrive\Belgeler"
DOSSIER_LOGS = r"C:\Users\Manel\OneDrive\Bureau\Automatisation"
DOSSIER_SANS_NOM = os.path.join(DOSSIER_A_SURVEILLER, "Sans nom")
DOSSIER_PID = os.path.join(DOSSIER_LOGS, "Logs_PID")  # Dossier logs

# Barre de progression
def barre_de_chargement(duree, message):
    for _ in tqdm(range(duree), desc=message, ncols=100, ascii=True):
        time.sleep(1)


def creation_dossier_logs():
    if not os.path.exists(DOSSIER_PID):
        barre_de_chargement(5, "Création du dossier 'Logs_PID'")  # Barre de progression de 5 secondes
        os.makedirs(DOSSIER_PID)
        print(f"Dossier '{DOSSIER_PID}' créé avec succès.")
    else:
        print(f"Le dossier '{DOSSIER_PID}' existe déjà.")

def creation_dossier_sans_nom():
    if not os.path.exists(DOSSIER_SANS_NOM):
        barre_de_chargement(5, "Création du dossier 'Sans nom'")  # Barre de progression de 5 secondes
        os.makedirs(DOSSIER_SANS_NOM)
        print(f"Dossier '{DOSSIER_SANS_NOM}' créé avec succès.")
    else:
        print(f"Le dossier '{DOSSIER_SANS_NOM}' existe déjà.")


# Ecrire les logs
def ecrire_pid():
    # Assure que le dossier existe avant d'écrire
    if not os.path.exists(DOSSIER_PID):
        print(f"Erreur : Le dossier '{DOSSIER_PID}' n'existe pas.")
    else:
        pid_file_path = os.path.join(DOSSIER_PID, "Surveillance-docs.txt")
        with open(pid_file_path, "w") as f:
            f.write(str(os.getpid()))
        print(f"Fichier PID écrit dans '{pid_file_path}'.")


class GestionnaireFichiers(FileSystemEventHandler):
    def on_modified(self, event):
        # Scanne le dossier avec barre de progression
        barre_de_chargement(5, "Vérification du dossier pour des fichiers non classés")
        
        for fichier in os.listdir(DOSSIER_A_SURVEILLER):
            if fichier.endswith('.docx') or fichier.endswith('.txt') or fichier.endswith('.pdf'):  # Word, Texte ou PDF
                chemin_fichier = os.path.join(DOSSIER_A_SURVEILLER, fichier)
                if not (fichier.startswith("Cours-") or fichier.startswith("Perso-") or fichier.startswith("IPSSI-")):  # Si le fichier ne commence pas par Cours- ou Perso-
                    nouveau_chemin = os.path.join(DOSSIER_SANS_NOM, fichier)
                    shutil.move(chemin_fichier, nouveau_chemin)
                    print(f"Fichier {fichier} déplacé dans 'Sans nom'.")

# Initialisation de l'observation du dossier Documents
event_handler = GestionnaireFichiers()
observer = Observer()
observer.schedule(event_handler, DOSSIER_A_SURVEILLER, recursive=False)

# Lancer l'observation
observer.start()

try:
    # Vérifier et créer les dossiers nécessaires
    creation_dossier_sans_nom()  
    ecrire_pid() 
    
    # Boucle infinie pour la surveillance et vérification des dossiers
    while True:
        time.sleep(300) #5min
        # Vérifier que les dossiers existent toujours
        if not os.path.exists(DOSSIER_PID) or not os.path.exists(DOSSIER_SANS_NOM):
            print("Erreur : Les dossiers 'Logs_PID' ou 'Sans nom' n'existent plus. Arrêt de l'automatisation.")
            break  # Sortir de la boucle si l'un des dossiers n'existe pas
except KeyboardInterrupt:
    observer.stop()

observer.join()