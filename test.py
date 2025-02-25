import socket
import json

def test_client(host='localhost', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        test_data = json.dumps([{"Name": "Dell", "Date": "2025-02-09 11:33:19"}])

        print("Original Data:")
        print(test_data)

        client_socket.sendall(test_data.encode('utf-8'))
        response = client_socket.recv(4000).decode('utf-8')
        print("Response:")
        print(response)

if __name__ == "__main__":
    test_client()