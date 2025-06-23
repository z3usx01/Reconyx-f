import requests

def get_wayback_urls(domain):
    try:
        url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey"
        res = requests.get(url, timeout=10).json()

        return [entry[0] for entry in res[1:]] if len(res) > 1 else ["No archived URLs found."]
    except Exception as e:
        return [f"Error: {e}"]
