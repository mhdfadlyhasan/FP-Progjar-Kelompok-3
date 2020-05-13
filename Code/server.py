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
            if message:
                print (addr[2] + ': ' + message[:-1])
                message_to_send = addr[2] + ': ' + message
                broadcast(message_to_send, conn,addr[2],username_target)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection,username_sender,username_target):
    for clients,data in list_of_clients:
        if(data == username_target):
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
    username = conn.recv(2048).decode()
    temp = list(addr)
    temp.append(username)
    addr = tuple(temp)
    list_of_clients.append((conn,addr[2]))
    print (addr[2] + ' has joined the chat!')
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    
conn.close()