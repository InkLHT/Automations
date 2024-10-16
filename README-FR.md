> *Ce code contient probablement des erreurs, mais il est simplement à des fins de test et de fun ! Il n'est qu'une base qui sera améliorée à l'avenir. Les autres peuvent l'utiliser comme point de départ et l'améliorer également. Il contient sûrement des erreurs, donc n'hésitez pas à contribuer et à proposer des améliorations.*
# Surveillance de Fichiers en Python
L'objectif de ce script Python est de surveiller un dossier donné et d'automatiser certaines actions, comme déplacer des fichiers en fonction de leur type ou de leur nom. Le script utilise watchdog pour détecter en temps réel tout changement dans le dossier, et il organise automatiquement les fichiers non classés dans un sous-dossier.

### QU'EST-CE QUE WATCHDOG ET TQDM ?
Watchdog est une bibliothèque Python qui permet de surveiller les systèmes de fichiers en temps réel. Elle détecte tout changement apporté à un dossier ou fichier et déclenche des événements spécifiques. Cette fonctionnalité est utile pour automatiser les tâches liées aux fichiers, telles que l'organisation ou la détection d'anomalies.

TQDM est une bibliothèque Python qui permet d'afficher une barre de progression dans le terminal.

### FONCTIONNALITÉS DU SCRIPT
- Surveillance en temps réel d'un dossier pour détecter les modifications, ajouts ou suppressions de fichiers.
- Organisation automatique des fichiers détectés (par exemple, déplacement des fichiers qui ne suivent pas une convention de nommage spécifique).
- Journaux (logs) : Écriture des événements et du processus dans un fichier (dans mon cas, Surveillance-docs.txt).
- Barre de progression pour indiquer visuellement la création d'un dossier ou l'analyse des fichiers.
- Vérification continue toutes les 5 minutes pour s'assurer que les dossiers nécessaires existent toujours.

### QUEL OS (SYSTÈME D'EXPLOITATION) POUR L'UTILISER ?
Le script peut fonctionner sur Windows et Linux/macOS ! Il suffit simplement d'ajuster les chemins d'accès.

# Structure du Script
### VARIABLES PRINCIPALES
- `DOSSIER_A_SURVEILLER` : Le dossier principal à surveiller.
- `DOSSIER_LOG` : Le dossier où sont enregistrés les journaux (logs).
- `DOSSIER_SANS_NOM` : Sous-dossier pour les fichiers non classés.
- `FOLDER_PID` : Dossier où le fichier PID (ID du processus) est enregistré.

# Prérequis
### 1. Python 3 ou plus
Assurez-vous que **Python 3 ou plus** est installé sur votre système. Vous pouvez télécharger Python depuis leur site officiel. Pour vérifier si Python est déjà installé, ouvrez un terminal ou une invite de commandes (cmd) et exécutez :
```bash
python --version
```

### 2. Bibliothèques Python
Pour utiliser le script, vous devez installer les bibliothèques Python `watchdog` et `tqdm`, vous pouvez le faire en exécutant la commande suivante dans un éditeur de texte de votre choix (dans mon cas, Visual Studio Code) :
```bash
pip install watchdog tqdm
```

### 3. Permissions du système
Sur certains systèmes d'exploitation, vous devrez peut-être exécuter le script avec des privilèges élevés (en tant qu'administrateur ou avec sudo sur Linux). Le script a besoin des permissions suivantes :
- Lire et écrire dans les dossiers définis par `DOSSIER_A_SURVEILLER` et `DOSSIERS_LOGS`.
- Créer ou déplacer des fichiers dans les dossiers.
