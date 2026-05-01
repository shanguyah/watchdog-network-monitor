<div align="center">
  <img src="https://img.shields.io/badge/WATCHDOG--NETWORK-SENTINEL-gold?style=for-the-badge&logo=opsgenie" alt="Watchdog Logo" />
  
  <h1>🛡️ WATCHDOG-NETWORK</h1>
  <p><i>Professional Network Uptime Monitoring Utility</i></p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" />
    <img src="https://img.shields.io/badge/Security-Asset%20Tracking-red?style=flat-square" />
    <img src="https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=flat-square" />
  </p>
</div>

---

### 💎 The Vision
**WatchDog** is a high-performance, single-script sentinel designed for developers and security specialists[cite: 1, 2]. Built with a focus on a "zero-footprint" philosophy, it provides real-time visibility into the health of local and remote infrastructure without requiring external dependencies[cite: 3].

---

### 🛠️ Configuration & Usage

WatchDog is designed for immediate "plug-and-play" deployment.

1.  **Define Targets**: Open `monitor.py` and add your IP addresses or domains to the `HOSTS` array:
    ```python
    HOSTS = ["192.168.1.1", "8.8.8.8", "yourserver.com"]
    ```
2.  **Launch**: Execute the script from your terminal[cite: 1, 3]:
    ```bash
    python monitor.py
    ```
    *(Note: Linux users may require `sudo` for ICMP authorization[cite: 1, 3].)*

---

### 🏗️ Technical Architecture
The utility is engineered for high accuracy across diverse network environments[cite: 2].

*   **Core Engine**: Leverages the Python `subprocess` module to interface directly with system-level ICMP protocols[cite: 1, 3].
*   **Abstraction Layer**: Automatically detects the host OS (Windows, Linux, macOS) and adjusts ping arguments accordingly[cite: 1, 3].
*   **Zero-Dependency Logic**: Built strictly using standard libraries (`os`, `platform`, `time`), ensuring it runs on any system with Python 3.x installed[cite: 1, 3].

---

<div align="center">
  <p><b>Developed by Valentine Shyanguya Ong’ayo</b></p>
  <p><i>Software Developer | Security Specialist</i></p>
  
  <a href="https://github.com/shanguyah">
    <img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" />
  </a>
</div>
