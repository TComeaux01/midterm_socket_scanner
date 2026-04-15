import socket
import time

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))

        if result == 0:
            return True
        return False

    except Exception:
        return False

    finally:
        sock.close()

def run_scanner():
    host = input("Enter host (e.g., 127.0.0.1 or scanme.nmap.org): ")

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("[ERROR] Invalid port range.")
            return

    except ValueError:
        print("[ERROR] Ports must be numbers.")
        return

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        time.sleep(0.1)  # ethical delay

if __name__ == "__main__":
    run_scanner()
