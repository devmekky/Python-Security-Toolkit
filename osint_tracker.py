import requests
import concurrent.futures
import sys

# List of popular platforms and their URL structures for username checking
PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Twitter/X": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}/about.json",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "SoundCloud": "https://soundcloud.com/{}"
}

def check_profile(platform, url, username):
    target_url = url.format(username)
    # Headers to mimic a real browser and avoid blocks
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        # Check if profile exists based on status code (200 OK)
        if response.status_code == 200:
            print(f"[+] Found ({platform}): {target_url}")
        else:
            print(f"[-] Not Found ({platform})")
    except requests.RequestException:
        print(f"[!] Error connecting to {platform}")

def main():
    print("-" * 60)
    print("[*] Modern OSINT Username Footprinter Tool")
    print("-" * 60)
    
    username = input("Enter target username to search: ").strip()
    if not username:
        print("[!] Username cannot be empty.")
        sys.exit()

    print(f"\n[*] Searching for username '{username}' across platforms...\n")
    
    # Using ThreadPoolExecutor for fast multi-threaded requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for platform, url in PLATFORMS.items():
            executor.submit(check_profile, platform, url, username)
            
    print("\n" + "-" * 60)
    print("[*] Scan completed successfully.")
    print("-" * 60)

if __name__ == "__main__":
    main()