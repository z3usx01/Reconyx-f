import requests

def shodan_lookup(ip, api_key):
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
        res = requests.get(url, timeout=10).json()

        return {
            "IP": res.get("ip_str", ""),
            "Organization": res.get("org", ""),
            "OS": res.get("os", ""),
            "Ports": res.get("ports", [])
        }
    except Exception as e:
        return {"Error": str(e)}
