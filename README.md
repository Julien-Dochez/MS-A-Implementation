# MS-A-Implementation

Requirements:
- python installed
- import socket and json into main program

A. Steps to Request Data:
- Create a Socket
Example Code:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket

    This line will create a socket and name it client_socket

- Connect to the Microservice
Example Code:

    client_socket.connect((host, port))

    Your program will have to define a host and port number, which will have to be same as the microservice's host and port number

    def test_client(host='localhost', port=5000):

    This line of code creates a function that defines the host and port number. test_client() can be used to call the function

- Create a list of dictionaires using json.dumps()
Example Code:

    test_data = json.dumps([{"Name": "Dell", "Date": "2025-02-09 11:33:19"}])

    This line creates a list of dictionaries named test_data.

    test_data = json.dumps([
        {"Name": "Dell", "Date": "2025-02-09 11:33:19"},
        {"Name": "HP", "Date": "2024-12-25 08:15:00"},
        {"Name": "Lenovo", "Date": "2023-10-31 14:20:45"},
        {"Name": "Apple", "Date": "2026-01-01 09:00:00"}
    ])

    This shows how more dictionaires can be added to the list in the same format.

- Send the Data  
Example Code:

    client_socket.sendall(test_data.encode('utf-8'))

    This line will send the list of dictionaires called "test_data" to the microservice

Example Call

if __name__ == "__main__":
    test_client()

The microservice must be running on the same localhost and port for this call to function


B. How to Receive Data:
- Connect to the Microservice
Example Code:

    client_socket.connect((host, port))

    With the same client_socket you created to request data, use it to connect to the microservice which is on the same host and port as your main program

- Receive the Response
Example Code:

    response = client_socket.recv(4000).decode('utf-8')

    Use this line of code to receive the response from the microservice, which is now saved in "response"

Example Call

if __name__ == "__main__":
    start_server()

This example call is used in the microservice which starts the microservice itself.