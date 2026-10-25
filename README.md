Last login: Sun Oct 25 10:57:05 on ttys000
d4lcaso@Skylynns-Air ~ % # 📱 iOS IPSW Research & Extraction Assistant

A lightweight Python utility designed for security research and firmware analysis. This script automates the process of connecting an iOS device via USB to retrieve hardware identifiers, extracting an `.ipsw` container, and re-packing files after analysis.

## ✨ Features
* **Device Linker:** Automatically detects connected iOS hardware via `usbmuxd` and outputs configuration info.
* **Extraction Engine:** Unpacks compressed `.ipsw` components locally.
* **Repack Utility:** Bundles modified components back into an archive.

## 🚀 Setup Instructions

### 1. Install Prerequisites
Ensure you have Python 3.8+ installed on your computer.

Install the required library for device communication:
```bash
pip install -r requirements.txt
```

*Note for Windows users:* You must have **iTunes** installed from Apple's website (not the Microsoft Store) so that the computer has the necessary USB multiplexer (`usbmuxd`) drivers to detect the device.

### 2. Usage
1. Place your target firmware file in the root folder of this project.
2. Open your terminal or command prompt in this folder.
3. Run the script:
   ```bash
   python app.py
   ```
4. Follow the on-screen prompts to view connected device data, pause for folder edits, and compile the final package.






















