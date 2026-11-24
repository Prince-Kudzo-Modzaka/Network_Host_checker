import subprocess

def check_hosts(filename):
    # To print a summary report at the end.
    print("--- SUMMARY REPORT ---")
    online_count = 0
    offline_count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                # To remove invisible newline characters and skipping empty lines.
                host = line.strip()
                if not host:
                    continue
                
                # Using subprocess to run the OS's native ping command.
                # Using stdout=DEVNULL and stderr=DEVNULL to give clearn and nice output
                # NOTE: '-n' is for Windows. If using Linux/Kali, change to '-c'.
                result = subprocess.run(
                    ['ping', '-n', '1', host], 
                    stdout=subprocess.DEVNULL, 
                    stderr=subprocess.DEVNULL
                )
                
                # A successful ping will output code of 0 meaning the host is alive.
                if result.returncode == 0:
                    print(f"✅ {host:<15} | STATUS: ONLINE")
                    online_count += 1
                else:
                    print(f"🛑 {host:<15} | STATUS: OFFLINE / UNREACHABLE")
                    offline_count += 1
                    
        print("\n--- SUMMARY ---")
        print(f"Total Scanned: {online_count + offline_count}")
        print(f"Online: {online_count} | Offline: {offline_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    
    check_hosts('host_file.txt')