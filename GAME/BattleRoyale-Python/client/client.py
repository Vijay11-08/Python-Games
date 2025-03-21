import socket

SERVER_IP = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

while True:
    message = input("Send: ")
    client.send(message.encode())
    response = client.recv(1024).decode()
    print("Server:", response)
