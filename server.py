#!/usr/bin/python3
def process_command(command):
    try:
        querylist = command.split()
        query = querylist.pop(0)
        print(querylist, query)
        if query not in commands_list:
            return query + ' is not a known command. Type "help" for a list of known commands'
        else:
            return 'Command found\n*Add if-elif-else blocks here to handle the respective command.'
    except:
        return 'Error in command'

help_text = 'This is a simple server-client program. You can use the following commands:\nversion\nabout\nhelp'
commands_list = {'version':'1.0.0',
                 'about':'Created by Kaushal',
                 'help':help_text}
import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(('localhost', port))
s.listen(5)
client_socket, client_address = s.accept()
while True:
    try:
        received_data = client_socket.recv(1024).decode()
        if not received_data:
            break
        data = process_command(received_data)

        client_socket.send(data.encode())
    except BrokenPipeError:
        pass
client_socket.close()
