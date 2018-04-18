#!/usr/bin/python3
import socket

#Create a socket
s = socket.socket()

#Set this to the address of the server
host = 'localhost'
port = 8080

try:
    #Try to connect with the server, if cannot connect dsplay error and exit
    s.connect((host, port))

    while True:
        #Get the input message
        message = input('->')

        if message.lower() == 'quit':
            break

        #Send the input command to the server
        s.send(message.encode())

        #Receive response from the server
        message = s.recv(1024).decode()
        print(message)
    #Close the socket
    s.close()
    
except ConnectionRefusedError:
    print('Failed to connect. Please check if the server is running')
