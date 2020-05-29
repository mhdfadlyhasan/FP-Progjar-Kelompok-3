import socket
import select
import sys
import threading
import os
import django
import datetime
from dotenv import load_dotenv

load_dotenv(verbose=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyNet.settings')
django.setup()
from django.db import models
# from django.contrib.auth.models import User
from chat.models import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []
room_example = []
unique_id = ""

def clientthread(conn, addr):
    
    while True:
        try:
            message = conn.recv(2048).decode()

            # Client berhenti
            if (message[:6] == '<quit>'):
                print('Client with ID ' + str(addr[3]) + ' has left the application')

            elif (message[:8] == '<create>'):
                split = message.split(' ')
                # print(split[1])

                # code create room di DB disini
                room = Room(RoomName=split[1])
                room.save()

                print('Room Created with ID ' + split[1]) 
                memb = int(addr[3])
                member = Room_Acc.objects.create(AccID=memb, RoomID=room)
                

                # Room dummy untuk testing awal
                room_example.append((conn, str(addr[3])))

            elif (message[:8] == '<invite>'):
                split = message.split(' ')
                invite_id = split[1]

                for client in list_of_clients:
                    if (client[1] == invite_id[:-1]):
                        print("Receiver ID: " + client[1])
                        client_conn = client[0]
                        # print(client_conn)

                room_example.append((client_conn, invite_id[:-1])) 
                print (room_example)

            elif (message[:6] == '<join>'):
                print('join')

            # Terima id orang yang akan di personal chat
            elif (message[:4] == '<id>'):
                unique_id = message[4:len(message)]
                print(unique_id)
                #tunjukkan list pesan ke pengguna! list didapat dari dataase
                message = "selamat datang, riwayat pesan anda "
                conn.send(message.encode())

            # Send message personal chat
            elif (message[:10] == '<personal>'):
                print (addr[2] + ':' + message[10:-1])
                message_to_send = addr[2] + ':' + message[10:-1]
                personal_chat(message_to_send, conn, addr[3], unique_id)
                #put to db

            # Send message personal chat
            elif (message[:7] == '<group>'):
                message_to_send = addr[2] + ':' + message[7:-1]
                sender_id = str(addr[3])
                print (addr[2] + ':' + message[7:-1])

                # Code broadcast dengan room id disini

                # broadcast dengan room dummy
                broadcast(message_to_send, conn, sender_id)

                #put to db
                try:
                    msg_db = Message.objects.create(room=room,msg=message[7:-1],AccSent=addr[3],getTime=datetime.datetime.now())
                    print('success')
                except:
                    print('error')
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

def broadcast(message, connection, sender_id):
    for clients, unique_id in room_example:
        if unique_id != sender_id:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove_group(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def remove_group(connection):
    if connection in room_example:
        room_example.remove(connection)

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
    # print(conn)
    threading.Thread(target=clientthread, args=(conn, addr)).start()
    
conn.close()