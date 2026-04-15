import socket

def start_server():
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection established with {addr}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                print("[SERVER] Client disconnected.")
                break

            print(f"[SERVER] Received: {data}")
            response = f"Server received: {data}"
            conn.send(response.encode())

    except Exception as e:
        print(f"[SERVER ERROR] {e}")

    finally:
        server_socket.close()
        print("[SERVER] Server shut down.")

if __name__ == "__main__":
    start_server()
