# 🛡️ CyberShield v1.0

Advanced Personal Cybersecurity Toolkit built using Flask, Python, and Networking Libraries.

---

# 📌 Overview

CyberShield is a multi-functional cybersecurity platform designed for:
- Network analysis
- Threat monitoring
- Packet inspection
- DNS intelligence
- WHOIS reconnaissance
- Security logging

The project combines multiple cybersecurity tools into one professional dashboard interface.

---

# 🚀 Features

## ✅ Dashboard
- Security overview
- Activity monitoring
- Threat summary
- Recent scan logs

---

## ✅ Port Scanner
- Scan open ports
- Detect active services
- TCP port analysis

---

## ✅ Network Scanner
- Discover connected devices
- Identify local network hosts
- Device monitoring

---

## ✅ Packet Sniffer
- Capture live packets
- Analyze TCP/UDP/ICMP traffic
- Real-time packet monitoring

---

## ✅ DNS Analyzer
- A Records
- MX Records
- TXT Records
- NS Records
- CNAME Records

---

## ✅ WHOIS Lookup
- Registrar information
- Domain expiration
- Domain creation date
- Name server analysis

---

## ✅ Threat Monitor
- High TCP traffic detection
- Suspicious IP activity
- Basic IDS functionality
- Real-time alert generation

---

## ✅ Logs System
- SQLite database
- Activity tracking
- Security event history
- Scan logging

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Flask | Web Framework |
| HTML/CSS | Frontend UI |
| Scapy | Packet Sniffing |
| Nmap | Port Scanning |
| SQLite | Database |
| DNSPython | DNS Analysis |
| Python-WHOIS | WHOIS Lookup |

---

# 📂 Project Structure

```bash
CyberShield/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── db.py
│   └── logs.db
│
├── scanner/
│   ├── port_scanner.py
│   ├── network_scanner.py
│   ├── packet_sniffer.py
│   ├── dns_analyzer.py
│   ├── whois_lookup.py
│   ├── threat_monitor.py
│   └── threat_data.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── script.js
│       └── charts.js
│
└── templates/
    ├── layout.html
    ├── dashboard.html
    ├── port_scanner.html
    ├── network_scanner.html
    ├── packet_sniffer.html
    ├── dns_analyzer.html
    ├── whois_lookup.html
    ├── threat_monitor.html
    └── logs.html
