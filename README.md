# Python Security Toolkit 🛡️

A collection of custom cybersecurity tools, networking scripts, and automation utilities built using Python. This repository is dedicated to practical information security development, reconnaissance, and network scanning.

## 🛠️ Tools Included

### 1. Multi-Threaded Port Scanner (`port_scanner.py`)
A fast network port scanner built using Python's `socket` and `threading` libraries. It allows security analysts and network administrators to quickly scan target hosts for open ports.

* **Features:**
  * Multi-threading support for fast execution.
  * Customizable target IP and port range.
  * Clean and professional error/exception handling.

### 2. Subdomain Enumerator (`sub_enum.py`)
A reconnaissance tool designed to discover active subdomains for a given target domain using HTTP requests and a predefined wordlist.

* **Features:**
  * Automated scanning of common subdomains.
  * Exception handling for connection errors and timeouts.
  * Clean user interruption support.

## 🚀 Usage Example

Run the scripts from your terminal:
```bash
python port_scanner.py
python sub_enum.py
