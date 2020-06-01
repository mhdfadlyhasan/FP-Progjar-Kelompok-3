import socket
import select
import sys
import msvcrt
# from .CRUDtoDatabase import dbHelper

# #init db
# database_tools = dbHelper()

class GroupChatClientModel:
    server = None
    username = ''
    your_id = ''
    connected = False
    list_pesan_sekarang = []
    current_chat_room = 0

    def __init__(self):
        if self.connected == False:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ip_address = '127.0.0.1'
            self.port = 8081
            self.server.connect((self.ip_address, self.port))
            self.connected = True

            # # Input username & ID sendiri
            # self.username = input("Please enter your username: ")
            # self.your_id = input("Please enter your ID: ")
        
            # # Send username + id
            # packet = self.username + ',' + self.your_id
            # self.server.send(packet.encode())

        elif self.connected == True:
            print('Connected to server')
    
    # Send login input
    def send_login(self, username, password):
        self.username = username
        self.your_id = password
        packet = self.username + ',' + self.your_id
        self.server.send(packet.encode())

    # Function terima input dari user
    def group_chat(self):

        if True:
            sockets_list = [self.server]

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

                    # testing: follow up <createpersonal>
                    # sorry if broke the whole program
                    if (message[:16] == '<personalroomid>'):
                        split = message.split(',')
                        print ('Room ID is yes ' + split[1])
                        current_chat_room = split[1]
                    else:
                        self.list_pesan_sekarang.append(message)
                        print(message)

                else:
                    message = temp
                    # Format <create> ID_room
                    if (message[:8] == '<create>'):
                        split = message.split(',')
                        print ('You created a room with ID ' + split[1])
                        self.server.send(message.encode())

                    # testing: Format <createpersonal> ID_user
                    elif (message[:16] == '<createpersonal>'):
                        split = message.split(',')
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
    def group_chat_get_message(self,object_gui,room_id):
        
        if(len(self.list_pesan_sekarang)>0):#cek apakah lagi dalam chat list sekarang
            
            pesan = self.list_pesan_sekarang[0].split("<idroom>")
            if(int(pesan[1])==int(room_id)):
                object_gui.message_list.append(pesan[0])
            self.list_pesan_sekarang.pop(0)