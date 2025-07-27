from ip_checker import check_ip

def main():
    ip = input("Enter IP address to check: ").strip()
    check_ip(ip)

if __name__ == "__main__":
    main()
