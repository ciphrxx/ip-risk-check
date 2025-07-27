from apis.ipwhois import check_ipwhois, get_user_country

def check_ip(ip):
    print(f"\n Checking IP: {ip}\n")

    user_country = get_user_country()
    ip_data = check_ipwhois(ip)

    if not ip_data:
        print("Failed to retrieve IP data. Please try again")
        return

    print("Connection type:")
    print(f"• Proxy use: {'Yes' if ip_data['proxy'] else 'No'}")
    print(f"• Hosted on a server or cloud provider: {'Yes' if ip_data['hosting'] else 'Not enough metadata to confirm'}")
    print(f"• Tor network: {'Yes' if ip_data['tor'] else'No'}")

    print(f"\nLocation: {ip_data['country']} ({ip_data['country_code']} | ISP: {ip_data['isp']}")

    risk = sum([
        ip_data["proxy"],
        ip_data["hosting"],
        ip_data["tor"],
        user_country and user_country != ip_data["country_code"]
    ])

    if user_country and user_country != ip_data["country_code"]:
        print(f"Geo mismatch: IP is in {ip_data['country_code']}, you are in {user_country}")
        print("Note: This check may be inaccurate if you are using a VPN or proxy.")

    verdict = ["✅ Safe", "⚠️ Low", "⚠️ Suspicious", "❌ High", "❌ High"][min(risk, 4)]
    print(f"\nRisk Score: {risk}/4 → {verdict}")