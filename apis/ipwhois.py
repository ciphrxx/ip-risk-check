import requests

def get_user_country():
    response = requests.get("https://ipwho.is/")
    if response.status_code == 200:
        data = response.json()
        return data.get("country_code")
    return None

def check_ipwhois(ip):
    response = requests.get(f"https://ipwho.is/{ip}")
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            return {
                 "country": data.get("country", "Unknown"),
                "country_code": data.get("country_code", "Unknown"),
                "isp": data.get("connection", {}).get("isp", "Unknown"),
                "proxy": data.get("security", {}).get("proxy", False),
                "hosting": data.get("hosting", False),
                "tor": data.get("security", {}).get("tor", False)
            }
    return None
