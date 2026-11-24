#  Network Asset & Uptime Checker

##  Project Overview
In IT and Cybersecurity, maintaining an inventory of active network assets is critical or very important. This Python tool that I have created automates the process of scanning a list of IP addresses or domain names to determine which of them are online. This simulates the basic functionality of network discovery tools used by SOC analysts and system administrators to identify potential outages or network misconfigurations.

##  Technical Skills Demonstrated
*   **Subprocess Management:** Interfaced Python with the underlying operating system's ICMP (Ping) utility.
*   **Error Handling:** Implemented `try/except` blocks to handle missing files and empty lines.
*   **Terminal Formatting:** Utilized ANSI escape codes and emojis to colorize the terminal output (Green for Online, Red for Offline) for instant readability.

1. Create a file named `host_file.txt` in the same directory as the script and add IP addresses or domains (one per line). 
   Example:
   ```text
   127.0.0.1
   8.8.8.8
   1.1.1.1
   192.168.1.1
   10.0.0.99
```
Run This Script.

python host_checking.py
```

## **The Result**

<img width="960" height="510" alt="pas2" src="https://github.com/user-attachments/assets/09dca8f7-5dc2-4a91-ac29-f9aaac2d1964" />
