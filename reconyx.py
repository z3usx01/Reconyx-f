import argparse
from modules.tech_detect import detect_technology
from modules.shodan_lookup import shodan_lookup
from modules.wayback_urls import get_wayback_urls

def main():
    parser = argparse.ArgumentParser(description="Reconyx OSINT CLI Tool")
    parser.add_argument("--url", help="URL to scan")
    parser.add_argument("--ip", help="IP for Shodan lookup")
    parser.add_argument("--shodan-key", help="Shodan API Key")
    args = parser.parse_args()

    if args.url:
        print("\n[+] Detecting Technologies...")
        print(detect_technology(args.url))

        print("\n[+] Fetching Wayback URLs...")
        for url in get_wayback_urls(args.url):
            print(url)

    if args.ip and args.shodan_key:
        print("\n[+] Shodan Lookup...")
        data = shodan_lookup(args.ip, args.shodan_key)
        for k, v in data.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    main()
