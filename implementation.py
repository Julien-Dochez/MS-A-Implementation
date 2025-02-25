import socket
import json

def process_data(data):
    try:
        data_list = json.loads(data)
        json_output = json.dumps(data_list, indent=2)
        return json_output
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format"})

def start_server(host='localhost', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    server_socket.settimeout(1.0)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            try:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024).decode('utf-8')
                    if not data:
                        break
                    response = process_data(data)
                    conn.sendall(response.encode('utf-8'))
            except socket.timeout:
                continue
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()