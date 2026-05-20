from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.dns import DNS

from scanner.threat_data import threat_alerts

from collections import defaultdict
from datetime import datetime


packets_data = []

ip_counter = defaultdict(int)

icmp_counter = 0
dns_counter = 0
tcp_counter = 0


def create_alert(threat, severity, source):

    alert = {

        "time":
            datetime.now().strftime("%H:%M:%S"),

        "threat":
            threat,

        "severity":
            severity,

        "source":
            source

    }

    threat_alerts.insert(0, alert)

    del threat_alerts[20:]


def process_packet(packet):

    global packets_data
    global icmp_counter
    global dns_counter
    global tcp_counter

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"

        # TCP
        if packet.haslayer(TCP):

            protocol = "TCP"

            tcp_counter += 1

            if tcp_counter > 15:

                create_alert(
                    "High TCP Traffic",
                    "MEDIUM",
                    src_ip
                )

        # UDP
        elif packet.haslayer(UDP):

            protocol = "UDP"

        # ICMP
        elif packet.haslayer(ICMP):

            protocol = "ICMP"

            icmp_counter += 1

            if icmp_counter > 10:

                create_alert(
                    "Possible ICMP Flood",
                    "HIGH",
                    src_ip
                )

        # DNS
        elif packet.haslayer(DNS):

            protocol = "DNS"

            dns_counter += 1

            if dns_counter > 10:

                create_alert(
                    "DNS Flood Detected",
                    "MEDIUM",
                    src_ip
                )

        ip_counter[src_ip] += 1

        # Suspicious IP Activity
        if ip_counter[src_ip] > 20:

            create_alert(
                "Suspicious IP Activity",
                "HIGH",
                src_ip
            )

        packet_info = {

            "source": src_ip,
            "destination": dst_ip,
            "protocol": protocol

        }

        packets_data.insert(0, packet_info)

        del packets_data[50:]


def start_sniffing():

    global packets_data

    packets_data = []

    sniff(
        prn=process_packet,
        count=50,
        store=False
    )

    return packets_data
