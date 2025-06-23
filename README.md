Reconyx
An OSINT CLI tool with modular structure to perform:

Technology detection (like Wappalyzer)

Shodan IP lookup

Archived URL fetch from Wayback Machine

Installation
git clone https://github.com/z3usx01/Reconyx.git
cd Reconyx
pip install -r requirements.txt

Usage
python3 reconyx.py [OPTIONS]

Options
--url Target URL for tech & Wayback detection
Example: --url https://example.com

--ip Target IP for Shodan lookup
Example: --ip 8.8.8.8

--shodan-key Shodan API key (used with --ip)
Example: --shodan-key YOUR_API_KEY

 You must use --ip and --shodan-key together for Shodan lookup.

Examples
Detect technologies & Wayback URLs:
python3 reconyx.py --url https://example.com

Run Shodan scan:
python3 reconyx.py --ip 8.8.8.8 --shodan-key SHODAN_API_KEY

Project Structure
Reconyx/
├── reconyx.py # Main CLI entry point
├── modules/
│ ├── tech_detect.py # Technology detection logic
│ ├── shodan_lookup.py # Shodan lookup logic
│ └── wayback_urls.py # Wayback Machine URL fetcher

To Do
Subdomain enumeration

Whois lookup

DNS & IP info

Output to JSON/text

CLI color styling

