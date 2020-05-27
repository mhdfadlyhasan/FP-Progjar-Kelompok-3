import socket
import select
import sys
import threading

class GroupChatServerModel:

    list_of_clients = []
    room_example = []
    unique_id = ""
    server = None
    
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ip_address = '127.0.0.1'
        port = 8081
        self.server.bind((ip_address, port))
        self.server.listen(100)

    def clientthread(self, conn, addr):
        
        while True:
            try:
                message = conn.recv(2048).decode()

                # Client berhenti
                if (message[:6] == '<quit>'):
                    print('Client with ID ' + str(addr[3]) + ' has left the application')

                elif (message[:8] == '<create>'):

                    split = message.split(' ')

                    # code create room di DB disini

                    # Room dummy untuk testing awal
                    self.room_example.append((conn, str(addr[3])))
                    print('Room Created with ID ' + split[1]) 

                elif (message[:8] == '<invite>'):
                    split = message.split(' ')
                    invite_id = split[1]

                    for client in self.list_of_clients:
                        if (client[1] == invite_id[:-1]):
                            print("Receiver ID: " + client[1])
                            client_conn = client[0]
                            # print(client_conn)

                    self.room_example.append((client_conn, invite_id[:-1])) 
                    # print (room_example)

                elif (message[:6] == '<join>'):
                    print('join')

                # Terima id orang yang akan di personal chat
                elif (message[:4] == '<id>'):
                    unique_id = message[4:len(message)]
                    print(unique_id)
                    #tunjukkan list pesan ke pengguna! list didapat dari dataase
                    message = "selamat datang, riwayat pesan anda "
                    conn.send(message.encode())

                # Send message group chat
                elif (message[:7] == '<group>'):
                    message_to_send = addr[2] + ':' + message[7:-1]
                    sender_id = str(addr[3])
                    print (addr[2] + ':' + message[7:-1])

                    # Code broadcast dengan room id disini

                    # broadcast dengan room dummy
                    self.broadcast(message_to_send, conn, sender_id)

                    #put to db

                else:
                    self.remove(conn)
            except:
                continue

    def broadcast(self, message, connection, sender_id):
        for clients, unique_id in self.room_example:
            if unique_id != sender_id:
                try:
                    clients.send(message.encode())
                except:
                    clients.close()
                    self.remove_group(clients)

    def remove(self, connection):
        if connection in self.list_of_clients:
            self.list_of_clients.remove(connection)

    def remove_group(self, connection):
        if connection in self.room_example:
            self.room_example.remove(connection)

    def server_start(self):
        conn, addr = self.server.accept()
        packet = conn.recv(2048).decode()

        # Menambahkan username dan id ke addr
        split = packet.split(',')
        # print(split)
        temp = list(addr)
        temp.append(split[0])
        temp.append(split[1])
        addr = tuple(temp)

        # Register id
        self.list_of_clients.append((conn, str(addr[3]))) 
        print (str(addr[2]) + ' has joined the chat with ID ' + str(addr[3]))
        # print(conn)
        threading.Thread(target=self.clientthread, args=(conn, addr)).start()

    def main(self):

        while True:
            self.server_start()

if __name__ == '__main__':
    model = GroupChatServerModel()
    model.main()
    
