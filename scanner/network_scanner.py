from scapy.all import ARP, Ether, srp
from datetime import datetime


def scan_network(ip_range):

    devices = []

    start_time = datetime.now()

    arp_request = ARP(pdst=ip_range)

    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in result:

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    end_time = datetime.now()

    total_time = end_time - start_time

    return {
        "devices": devices,
        "total_devices": len(devices),
        "scan_time": str(total_time),
        "network": ip_range
    }
