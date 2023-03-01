import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000

client.connect((HOST, PORT))

file = open("new_file", "wb")

client.send("send file".encode())
size: int = int(client.recv(1024).decode())

file_bytes = b""

received = 0
while received < size:
    data = client.recv(1024)
    file_bytes = file_bytes + data
    received = received + 1024

client.send("finished".encode())

file.write(file_bytes)
file.close()

client.close()
