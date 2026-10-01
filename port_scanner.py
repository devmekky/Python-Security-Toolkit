import socket
import threading
from datetime import datetime

# Target host input
target_host = input("Enter the IP address to scan: ")

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

def scan_port(port):
    try:
        # Create a socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_host, port)) # Returns 0 if the port is open
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except KeyboardInterrupt:
        print("\nExiting script.")
        exit()
    except socket.error:
        print("\nCould not connect to server.")
        exit()

# Scan the first 100 ports as a quick initial phase
for port in range(1, 101):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()