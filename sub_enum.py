import requests
import sys

def check_subdomains(domain):
    # A mini wordlist of common subdomains for scanning
    wordlist = ["www", "mail", "ftp", "localhost", "webmail", "admin", "test", "api", "dev", "shop"]
    
    print("-" * 50)
    print(f"[*] Starting Subdomain Enumeration for: {domain}")
    print("-" * 50)
    
    for sub in wordlist:
        # Construct the target subdomain URL
        sub_domain = f"http://{sub}.{domain}"
        
        try:
            # Send HTTP request to check if the subdomain exists
            response = requests.get(sub_domain, timeout=2)
            if response.status_code < 400:
                print(f"[+] Discovered Subdomain: {sub_domain}")
        except requests.ConnectionError:
            # Subdomain does not exist or is inactive
            pass
        except requests.Timeout:
            pass
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            sys.exit()

if __name__ == "__main__":
    target_domain = input("Enter target domain (e.g., example.com): ")
    check_subdomains(target_domain)