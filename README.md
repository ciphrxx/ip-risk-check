# 🛡️ Python IP Risk Check Script

### A simple Python tool that checks any IP address for signs of suspicious behavior using free public metadata.

---

#### Features

- Checks if the IP is using a **proxy**
- Detects if the IP is from a **cloud/hosting provider**
- Warns if the IP is from a **different country than yours**
- Calculates a simple **risk score (0 to 4)**
- CLI-based, easy to use, no API key required

---

#### Use Case

This tool helps you quickly check whether an IP address looks suspicious, even if it’s not listed in databases like VirusTotal or AbuseIPDB. For example, you can use it to verify if a strange IP your app connects to is coming from a server, proxy, or another country.

Useful for students, analysts, ethical hackers, or anyone learning how to investigate IP addresses with Python.

---

#### How It Works

When you enter an IP address, the tool sends a request to a free API service (ipwho.is) to retrieve public metadata about that IP. This includes details such as the country, internet service provider, whether the IP is using a proxy, if it's hosted on a cloud server, and in some cases, whether it belongs to the Tor network. 

At the same time, the tool checks your own IP address in the background to detect your current country. If the IP you're checking is located in a different country than your own, it is flagged as a geo mismatch. For each of the following indicators, proxy use, hosting provider, geo mismatch, and Tor network, the tool adds one point to a total risk score. The maximum score is 4, and a higher score means the IP may be more suspicious or anonymized. 

Note that Tor detection may not always work, as the API does not always include this metadata. 

Also, if you are using a VPN, your detected country may not reflect your real location, which can affect the geo mismatch result.

---

#### Technologies Used

[requests](https://pypi.org/project/requests/) - For retrieving data from [ipwho.is](https://ipwho.is)

---

#### How to Run

First, install the required Python library by opening a terminal and running the command '**pip install requests**'. This only needs to be done once.

Next, run the script by opening a terminal, navigating to the folder where the script is saved, and typing: 

**python cli.py**

The program will ask you to enter an IP address. If you don’t have one in mind, you can use a public example like **8.8.8.8** (Google DNS) just to test how it works.

After that, the tool will check the IP using free metadata from the internet. It will show you if the IP is using a proxy, if it looks like it’s hosted on a server, which country it’s from, and whether it’s from a different country than yours.

At the end, it gives a simple risk score from 0 to 4, so you can see how suspicious the IP might be.

---

#### Output

When you run the script and enter an IP address, the tool will show you a short summary with connection info, location, and a final risk score.

---

#### License

This project is licensed under the MIT License.

See the [LICENSE](./LICENSE) file for full details.

Copyright (c) 2025 Daniel Goropceanu

---

#### Author

Built by Daniel Goropceanu ([@ciphrxx](https://github.com/ciphrxx))

---



