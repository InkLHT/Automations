# Files Monitoring in Python
The purpose of this Python script is to monitor a given folder and automate certain actions, like moving files based on their type or name. The script uses watchdog to detect any changes in the folder in real time, and it automatically organizes unclassified files into a subfolder.

### WHAT IS WATCHDOG AND TQDM ?
Watchdog is a Python library that allows monitoring file systems in real time. It detects any changes made to a folder or file and triggers specific events. This feature is useful for automating file-related tasks, such as organizing or detecting anomalies.

TQDM is a Python library that allows us to display a progress bar in the terminal.

### FEATURES THE SCRIPT HAS
- Real-time folder monitoring to detect file modifications, additions, or deletions.
- Automatic organization of detected files (for example, moving files that don't follow a specific naming convention).
- Logs: Writing events and process to a file (in my case, Surveillance-docs.txt).
- Progress bar to visually indicate folder creation or file analysis.
- Continuous check every 5 minutes to ensure that the required folders still exist.

### WHAT OS (Operating System) SHOULD I USE ?
The script can work on Windows and Linux/macOS ! You just need to adjust the path.

# Script Structure
### MAIN VARIABLES
- `DOSSIER_A_SURVEILLER` (folder to watch): The main folder to monitor.
- `DOSSIER_LOG` (logs folder): The folder where the logs are stored.
- `DOSSIER_SANS_NOM` (unnamed folder): Subfolder for unclassified files.
- `FOLDER_PID`: Folder where the PID (process ID) file is written. 

# Prerequisites
### 1. Python 3 or more
Make sure you have **Python 3 or more** installed on your system. You can download Python via their website. To check if Python is already installed, open a terminal or command prompt (cmd) and run:
```bash
python --version
```

### 2. Python libraries
To use the script, you need to install the `watchdog` and `tqdm` Python libraries to display the progress bars and to monitor the file system. If you haven't yet installed these libraries, you can do it by running the following command in a text editor of your choice (in my case, Visual Studio Code):
```bash
pip install watchdog tqdm
```

### 3. System permissions
On some operating systems, you may need to run the script with elevated privileges (as administrator or with sudo on Linux). The script needs permissions to:
- Read and write to the folders defined by `DOSSIER_A_SURVEILLER` (folder to watch after) and `DOSSIERS_LOGS` (logs folder).
- Create or move files in the folders.
