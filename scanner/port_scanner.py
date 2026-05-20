import socket
from datetime import datetime


def scan_port(target, port):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            sock.close()

            return {
                "port": port,
                "service": service,
                "status": "OPEN"
            }

        sock.close()

    except:
        pass

    return None



def scan_target(target):

    results = []

    print(f"\n[+] Scanning Target: {target}\n")

    start_time = datetime.now()

    for port in range(1, 1025):

        result = scan_port(target, port)

        if result:
            results.append(result)

    end_time = datetime.now()

    total_time = end_time - start_time

    return {
        "target": target,
        "results": results,
        "total_ports": len(results),
        "scan_time": str(total_time)
    }
