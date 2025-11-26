import requests
import json
from config import IPINFO_TOKEN

def get_ip_info(ip):
    """Fetch IP info from ipinfo.io API."""
    try:
        url = f"https://ipinfo.io/{ip}/json?token={IPINFO_TOKEN}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return json.dumps(data)  # Store as string in DB
        else:
            return json.dumps({"error": "API error"})
    except Exception as e:
        return json.dumps({"error": str(e)})
