import socket
import select
import sys
import msvcrt

class GroupChatClientModel:

    isConnected = False
    server = None
    username = None

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        ip_address = '127.0.0.1'
        port = 8081

        # Input username & ID sendiri
        self.username = input("Please enter your username: ")
        your_id = input("Please enter your ID: ")
        self.server.connect((ip_address, port))
        self.isConnected = True

        # Send username + id
        packet = self.username + ',' + your_id
        self.server.send(packet.encode())

        return self.username

    # Function terima input dari user
    def group_chat(self, message):
  
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
    
    # Function terima message dari DB
    def ready_to_read(self):
        sockets_list = [self.server]

        while True:

            read_sockets, _ , exception_sockets = select.select(sockets_list, [], sockets_list)
           
            for socks in read_sockets:
                # Terima message
                if socks == self.server:
                    print('masuk')
                    message = socks.recv(2048).decode()
                    # print(message)      

    def main(self):
        username = self.connect()       
        self.ready_to_read()

if __name__ == '__main__':
    model = GroupChatClientModel()
    model.main()
        
