# Reconyx

An OSINT CLI tool with modular structure to perform:
- Technology detection
- Shodan lookup
- Wayback Machine archived URL fetch


Installation

git clone https://github.com/z3usx01/Reconyx.git
cd Reconyx
pip install -r requirements.txt
Usage
python3 reconyx.py [OPTIONS]
 Options
Option	Description	Example
--url	Target URL for technology & Wayback detection	--url https://example.com
--ip	Target IP address for Shodan lookup	--ip 8.8.8.8
--shodan-key	Your Shodan API key	--shodan-key YOUR_API_KEY

Use --ip and --shodan-key together for Shodan lookup.

 Examples
Detect technologies & Wayback URLs:

python3 reconyx.py --url https://example.com
Run Shodan scan:

python3 reconyx.py --ip 8.8.8.8 --shodan-key SHODAN_API_KEY
Modular Structure

Reconyx/
├── reconyx.py                # Main CLI entry point
├── modules/
│   ├── tech_detect.py        # Technology detection logic
│   ├── shodan_lookup.py      # Shodan lookup logic
│   └── wayback_urls.py       # Wayback Machine URL fetcher
 To Do 
Subdomain enumeration

Whois lookup

DNS & IP info

Output to JSON or text file

CLI color styling
