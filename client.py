#!/usr/bin/python3
import socket
s = socket.socket()
host = 'localhost'
port = 8080
running = True
try:
    s.connect((host, port))
    while True:
        message = input('->')
        if message.lower() == 'quit':
            break
        s.send(message.encode())
        message = s.recv(1024).decode()
        print(message)
    s.close()
except ConnectionRefusedError:
    print('Failed to connect. Please check if the server is running')
