WatchDog-Network Monitor
WatchDog is a lightweight, single-file Python utility designed to monitor network node uptime in real-time. It is built for simplicity—just drop the script into your environment, define your IPs, and start monitoring.

🚀 Features
Zero Dependencies: Uses only Python standard libraries.

Single-File Execution: Everything you need is contained within monitor.py.

Real-Time Feedback: Immediate status updates on your terminal.

Cross-Platform: Runs on Windows, macOS, and Linux.

🛠️ Setup & Usage
1. Clone or Download
Bash
git clone https://github.com/shanguyah/watchdog-network.git
cd watchdog-network
2. Configure Your Targets
Open monitor.py and update the TARGETS list with the devices you want to track (e.g., your gateway, Tenda routers, or web servers):

Python
# monitor.py
TARGETS = ["192.168.1.1", "8.8.8.8", "myserver.com"]
3. Run the Monitor
Bash
python monitor.py
Note for Linux Users: If you encounter permission errors with ICMP pings, run the script with: sudo python3 monitor.py.

📈 How It Works
The script utilizes the system's underlying ping command via the subprocess module to check connectivity. It interprets the exit codes to determine if a host is reachable, providing a clean, timestamped output directly to your console.

🛠️ Built With
Python 3

Subprocess & OS modules (Standard Library)
