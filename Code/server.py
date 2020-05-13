import socket
import select
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []
tuple_of_clients = []

def clientthread(conn, addr):
    username_target = conn.recv(2048).decode()
    print("Targeted Username " + username_target)
    while True:
        try:
            message = conn.recv(2048).decode()
            
            # Terima id orang yang akan di personal chat
            if (message[:4] == '<id>'):
                unique_id = message[-1]
                # print(unique_id)

            # Send message personal chat
            elif message:
                print (addr[2] + ':' + message[:-1])
                message_to_send = addr[2] + ':' + message
                personal_chat(message_to_send, conn, addr[3], unique_id)
            else:
                remove(conn)
        except:
            continue

def personal_chat(message, connection, sender_id, receiver_id):
    # Mencari id orang yang akan dikirimi pesan
    for clients, unique_id in list_of_clients:
        if unique_id == receiver_id:
            try:
                clients.send(message.encode())
            except:
                message = 'User with ID ' + str(receiver_id) + ' has left\n'
                print(message)
                clients.close()
                remove(clients)
                personal_chat(message, connection, sender_id, sender_id)

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)
    # for clients in list_of_clients:
    #     if clients != connection:
    #         try:
    #             clients.send(message.encode())
    #         except:
    #             clients.close()
    #             remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
        print("removed")

while True:
    conn, addr = server.accept()
    packet = conn.recv(2048).decode()

    # Menambahkan username dan id ke addr
    split = packet.split(',')
    # print(split)
    temp = list(addr)
    temp.append(split[0])
    temp.append(split[1])
    addr = tuple(temp)

    # Register id
    list_of_clients.append((conn, str(addr[3]))) 
    print (str(addr[2]) + ' has joined the chat with ID ' + str(addr[3]))
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    
conn.close()