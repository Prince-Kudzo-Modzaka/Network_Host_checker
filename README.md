#  Network Asset & Uptime Checker

##  Project Overview
In IT and Cybersecurity, maintaining an inventory of active network assets is critical. This Python tool automates the process of scanning a list of IP addresses or domain names to determine if they are online. This simulates the basic functionality of network discovery tools used by SOC analysts and system administrators to identify potential outages or network misconfigurations.

##  Technical Skills Demonstrated
*   **Subprocess Management:** Interfaced Python with the underlying operating system's ICMP (Ping) utility.
*   **Error Handling:** Implemented `try/except` blocks to gracefully handle missing files and empty lines.
*   **Terminal Formatting:** Utilized ANSI escape codes and emojis to colorize the terminal output (Green for Online, Red for Offline) for instant readability.

##  How to Run
1. Create a file named `host_file.txt` in the same directory as the script and add IP addresses or domains (one per line). Example:
   ```text
   8.8.8.8
   1.1.1.1
   192.168.1.1

Run This Script.

python host_checking.py
