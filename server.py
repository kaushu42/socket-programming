#!/usr/bin/python3

import socket

#This is for processing the received command.
#It takes text as input and breaks it down into commands
#Valid task is done for command and if the keyword is not recognized, error is displayed
def process_command(command):
    try:
        querylist = command.split() #split the input using spaces
        query = querylist.pop(0)    #get the first command by removing it from the list
        print(querylist, query)

        #If not a valid command
        if query not in commands_list:
            return query + ' is not a known command. Type "help" for a list of known commands'
        elif query == 'help':
            return help_text
        else:   #command is valid
            return 'Command found\n*Add if-elif-else blocks here to handle the respective command.'
    except: #if cannot split the input with spaces
        return 'Error in command'

#The text to display when the user types help
help_text = 'This is a simple server-client program. You can use the following commands:\nversion\nabout\nhelp'
#The list of available commands
commands_list = {'version':'1.0.0',
                 'about':'Created by Kaushal',
                 'help':help_text}

def main():
    #Create a socket
    s = socket.socket()

    #Select the required port
    port = 8080

    #Bind the socket to localhost:8080
    s.bind(('localhost', port))
    s.listen(5)

    #Accept incoming request from client
    client_socket, client_address = s.accept()

    #Keep on serving the client until the client exits
    while True:
        try:
            #Get input from the client
            received_data = client_socket.recv(1024).decode()

            #If no data is received, exit the program
            if not received_data:
                break

            #Handle the input and perform the required operation
            data = process_command(received_data)

            #Send appropriate response to the client
            client_socket.send(data.encode())

        except BrokenPipeError:
            pass

    #Need to close the client socket otherwise the current port becomes unusable
    client_socket.close()

if __name__ == '__main__':
    main()
