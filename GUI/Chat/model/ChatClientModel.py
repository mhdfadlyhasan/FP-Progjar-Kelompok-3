import socket
import select
import sys

class ChatClientModel:
    server = None
    username = ''
    password = ''
    your_id = ''
    connected = False
    list_pesan_sekarang = []
    current_chat_room = 0

    def __init__(self):
        # Connect ke server
        if self.connected == False:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ip_address = '127.0.0.1'
            self.port = 8081
            self.server.connect((self.ip_address, self.port))
            self.connected = True

        elif self.connected == True:
            print('Connected to server')

    # Send login ke server
    def send_login(self, username, password):
        self.username = username
        self.password = password
        packet = self.username + ',' + self.password
        self.server.send(packet.encode())

    # Function utama chat di client
    def chat(self):

        if True:
            sockets_list = [self.server]

            # Tunggu input
            ready_to_read = select.select([self.server], [], [], 0.1)[0] #delay diperkecil biar lebih responsive
            assert all(self.server.fileno() != -1 for server in ready_to_read)
            # Jika stdin tidak kosong
            if not sys.stdin.isatty():
                temp = sys.stdin.readline()
                if (str(temp) != ''):
                    ready_to_read.append(temp)

            for socks in ready_to_read:
                # Terima message
                if socks == self.server:
                    print('Received a message')
                    message = socks.recv(2048).decode()

                    # Jika personal chat ID
                    if (message[:16] == '<personalroomid>'):
                        split = message.split(',')
                        self.current_chat_room = split[1]

                    # Menempelkan pesan di list pesan
                    else:
                        self.list_pesan_sekarang.append(message)

                # Kirim message
                else:
                    message = temp

                    # Jika create group
                    if (message[:8] == '<create>'):
                        split = message.split(',')
                        print ('You created a room with name ' + split[1])
                        self.server.send(message.encode())

                    # Jika membuat personal chat
                    elif (message[:16] == '<createpersonal>'):
                        split = message.split(',')
                        print ('You created a room with ID ' + split[1])
                        self.server.send(message.encode())

                    # Jika melakukan invite 
                    elif (message[:8] == '<invite>'):
                        split = message.split(' ')
                        print ('You invited user with ID ' + split[1])
                        self.server.send(message.encode())   

                    # Jika menekan tombol member
                    elif (message[:8] == '<member>'):
                        split = message.split(' ')
                        print ('You requested member list from room ' + split[1])
                        self.server.send(message.encode())

                    # Kirim message biasa
                    else:
                        message = '<chats>' + message
                        self.server.send(message.encode())

                    sys.stdout.flush()

    # Untuk get message
    def chat_get_message(self,object_gui,room_id):
        
        # Mengecek apakah terdapat list pesan saat ini
        if(len(self.list_pesan_sekarang)>0):
            
            pesan = self.list_pesan_sekarang[0].split("<idroom>")
            if(int(pesan[1])==int(room_id)):
                # Menaruh pesan pada GUI
                object_gui.message_list.append(pesan[0])

            self.list_pesan_sekarang.pop(0)