import socket

def start_client():
    host = "127.0.0.1"
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"[CLIENT] Connected to server at {host}:{port}")

        message = input("Enter message to send: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"[CLIENT] Server response: {response}")

    except ConnectionRefusedError:
        print("[CLIENT ERROR] Cannot connect — server is not running.")

    except Exception as e:
        print(f"[CLIENT ERROR] {e}")

    finally:
        client_socket.close()
        print("[CLIENT] Client shut down.")

if __name__ == "__main__":
    start_client()
