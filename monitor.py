import os
import platform
import time

# Targets to monitor
targets = ["8.8.8.8", "1.1.1.1", "google.com", "192.168.0.1"] 

def check_status():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*40)
    print(f"📡 WATCHDOG NETWORK MONITOR")
    print(f"Scan started at: {time.ctime()}")
    print("="*40)
    
    for ip in targets:
        # Cross-platform ping command
        if platform.system().lower() == 'windows':
            # '-n' is for Windows, '> NUL' hides the technical details
            command = f"ping -n 1 {ip} > NUL 2>&1"
        else:
            # '-c' is for Linux/Mac, '> /dev/null' hides the technical details
            command = f"ping -c 1 {ip} > /dev/null 2>&1"
            
        response = os.system(command)
        
        # In os.system, 0 usually means success (Online)
        status = "✅ ONLINE" if response == 0 else "❌ OFFLINE"
        print(f"Target: {ip:15} | Status: {status}")
    
    print("="*40)
    print("Press Ctrl+C to stop...")

if __name__ == "__main__":
    try:
        while True:
            check_status()
            time.sleep(30) # Wait 30 seconds before next scan
    except KeyboardInterrupt:
        print("\n[!] WatchDog shutting down. Stay secure!")