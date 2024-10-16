# Files Monitoring in Python
The purpose of this Python script is to monitor a given folder and automate certain actions, like moving files based on their type or name. The script uses watchdog to detect any changes in the folder in real time, and it automatically organizes unclassified files into a subfolder.

### WHAT IS WATCHDOG ?
Watchdog is a Python library that allows monitoring file systems in real time. It detects any changes made to a folder or file and triggers specific events. This feature is useful for automating file-related tasks, such as organizing or detecting anomalies.

### FEATURES THE SCRIPT HAS
- Real-time folder monitoring to detect file modifications, additions, or deletions.
- Automatic organization of detected files (for example, moving files that don't follow a specific naming convention).
- Logs: Writing events and process to a file (in my case, Surveillance-docs.txt).
- Progress bar to visually indicate folder creation or file analysis.
- Continuous check every 5 minutes to ensure that the required folders still exist.

# Prerequisites
To use the script, you need to install the `watchdog` and `tqdm` Python libraries to display the progress bars and to monitor the file system.
