import socket
import select
import sys
import msvcrt

class GroupChatClientModel:

    isConnected = False
    server = None

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        ip_address = '127.0.0.1'
        port = 8081

        # Input username & ID sendiri
        username = input("Please enter your username: ")
        your_id = input("Please enter your ID: ")
        self.server.connect((ip_address, port))
        self.isConnected = True

        # Send username + id
        packet = username + ',' + your_id
        self.server.send(packet.encode())

    def group_chat(self):

        sockets_list = [sys.stdin, self.server]

        # Tunggu input
        ready_to_read = select.select([self.server], [], [], 0.01)[0] #delay diperkecil biar lebih responsive
        assert all(self.server.fileno() != -1 for self.server in ready_to_read)
        if msvcrt.kbhit(): ready_to_read.append(sys.stdin)

        for socks in ready_to_read:
            # Terima message
            if socks == self.server:
                message = socks.recv(2048).decode()
                print(message)
            
            # Send message
            else:
                message = sys.stdin.readline()
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
                    # print(message)
                    self.server.send(message.encode())
                    sys.stdout.flush()
                
                sys.stdout.flush()

    def main(self):
        self.connect()

        while True:
            self.group_chat()

if __name__ == '__main__':
    model = GroupChatClientModel()
    model.main()
        
