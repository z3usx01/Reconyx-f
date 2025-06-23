import requests

def detect_technology(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        tech = []

        if "wp-content" in res.text:
            tech.append("WordPress")
        if "Drupal.settings" in res.text:
            tech.append("Drupal")
        if "X-Powered-By" in res.headers:
            tech.append(res.headers["X-Powered-By"])

        return tech or ["Unknown"]
    except Exception as e:
        return [f"Error: {e}"]
