import socket
import select
import sys
import msvcrt
from .CRUDtoDatabase import dbHelper

#init db
database_tools = dbHelper()

class GroupChatClientModel:

    isConnected = False
    server = None
    username = None

    def __init__(self):
        if self.isConnected == False:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ip_address = '127.0.0.1'
            self.port = 8081
            self.server.connect((self.ip_address, self.port))
            self.isConnected = True
            
        elif self.isConnected == True:
            print('Connected to server')
        
    def connect(self):
        
        # Input username & ID sendiri
        self.username = input("Please enter your username: ")
        self.your_id = input("Please enter your ID: ")
    
        # Send username + id
        packet = self.username + ',' + self.your_id
        self.server.send(packet.encode())

        return self.username

    # Function terima input dari user
    def group_chat(self):

        while True:
            sockets_list = [sys.stdin, self.server]

            # Tunggu input
            ready_to_read = select.select([self.server], [], [], 0.1)[0] #delay diperkecil biar lebih responsive
            assert all(self.server.fileno() != -1 for server in ready_to_read)
            if not sys.stdin.isatty():
                temp = sys.stdin.readline()
                if (str(temp) != ''):
                    # print (temp)
                    ready_to_read.append(temp)

            for socks in ready_to_read:
                # Terima message
                if socks == self.server:
                    print('receive')
                    message = socks.recv(2048).decode()
                    # print(message)

                else:
                    message = temp

                    # Format <create> ID_room
                    if (message[:8] == '<create>'):
                        split = message.split(' ')
                        print ('You created a room with ID ' + split[1])
                        self.server.send(message.encode())

                    # Format <invite> ID_user
                    elif (message[:8] == '<invite>'):
                        split = message.split(' ')
                        print ('You invited user with ID ' + split[1])
                        self.server.send(message.encode())   

                    # Format <join> ID_room
                    elif (message[:6] == '<join>'):
                        split = message.split(' ')
                        print ('You joined room with ID ' + split[1])
                        self.server.send(message.encode())
                        
                    else:
                        message = '<group>' + message
                        print(message)
                        self.server.send(message.encode())

                    sys.stdout.flush()
        
