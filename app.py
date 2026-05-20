from flask import Flask, render_template, request

from scanner.port_scanner import scan_target
from scanner.network_scanner import scan_network
from scanner.packet_sniffer import start_sniffing
from scanner.dns_analyzer import get_dns_records
from scanner.whois_lookup import get_whois_info
from scanner.threat_monitor import get_threats
from database.db import init_db, add_log, get_logs

app = Flask(__name__)
init_db()

# DASHBOARD
@app.route("/")
def dashboard():

    logs_data = get_logs()

    total_logs = len(logs_data)

    total_threats = 0

    for log in logs_data:

        if "Threat" in log[1]:
            total_threats += 1

    recent_logs = logs_data[:5]

    return render_template(

        "dashboard.html",

        total_logs=total_logs,
        total_threats=total_threats,
        recent_logs=recent_logs

    )


# PORT SCANNER
@app.route("/port-scanner", methods=["GET", "POST"])
def port_scanner():

    scan_data = None

    if request.method == "POST":

        target = request.form.get("target")

        if target:

           scan_data = scan_target(target)

           add_log(
               "Port Scanner",
               "Port Scan",
               target,
               f"{scan_data['total_ports']} Open Ports"
    )

    return render_template(
        "port_scanner.html",
        scan_data=scan_data
    )


# NETWORK SCANNER
@app.route("/network-scanner", methods=["GET", "POST"])
def network_scanner():

    network_data = None

    if request.method == "POST":

        ip_range = request.form.get("ip_range")

        if ip_range:
            network_data = scan_network(ip_range)
            
            add_log(
               "Network Scanner",
               "Network Scan",
               ip_range,
               f"{network_data['total_devices']} Devices Found"
    )

    return render_template(
        "network_scanner.html",
        network_data=network_data
    )

# PACKET SNIFFER
@app.route("/packet-sniffer", methods=["GET", "POST"])
def packet_sniffer():

    packets = []

    if request.method == "POST":

        packets = start_sniffing()

    return render_template(
        "packet_sniffer.html",
        packets=packets
    )


# DNS ANALYZER
@app.route("/dns-analyzer", methods=["GET", "POST"])
def dns_analyzer():

    dns_records = None

    if request.method == "POST":

        domain = request.form.get("domain")

        if domain:
            dns_records = get_dns_records(domain)
            
            add_log(
              "DNS Analyzer",
              "DNS Lookup",
              domain,
              "DNS Records Retrieved"
    )

    return render_template(
        "dns_analyzer.html",
        dns_records=dns_records
    )


# WHOIS LOOKUP
@app.route("/whois-lookup", methods=["GET", "POST"])
def whois_lookup():

    whois_data = None

    if request.method == "POST":

        domain = request.form.get("domain")

        if domain:
            whois_data = get_whois_info(domain)
            
            add_log(
               "WHOIS Lookup",
               "WHOIS Query",
               domain,
               "WHOIS Information Retrieved"
    )

    return render_template(
        "whois_lookup.html",
        whois_data=whois_data
    )


# THREAT MONITOR
@app.route("/threat-monitor")
def threat_monitor():

    threats = get_threats()

    return render_template(
        "threat_monitor.html",
        threats=threats
    )


# LOGS
@app.route("/logs")
def logs():

    logs_data = get_logs()

    return render_template(
        "logs.html",
        logs=logs_data
    )


if __name__ == "__main__":
    app.run(debug=True)
