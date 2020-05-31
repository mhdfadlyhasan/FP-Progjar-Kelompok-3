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
from django.contrib.auth.models import User
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

def clientthread(conn, addr, list_of_clients):

    packet = conn.recv(2048).decode()
    # print (packet + " ini packet")

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
    # print(list_of_clients)
    room = 0
    while True:
        print(room)
        try:
            message = conn.recv(2048).decode()
            print('here')

            # Terima id orang yang akan di personal chat
            if (message[:4] == '<id>'):
                unique_id = message[4:len(message)]
                print(unique_id)
                #tunjukkan list pesan ke pengguna! list didapat dari dataase
                message = "selamat datang, riwayat pesan anda "
                conn.send(message.encode())
            # Client berhenti
            elif (message[:6] == '<quit>'):
                print('Client with ID ' + str(addr[3]) + ' has left the application')
            # join (implement plls)
            elif (message[:6] == '<join>'):
                print('join')
                split = message.split(' ')
                print('masuk create coba edit')
                print(split[1])
                # code create room di DB disini
                try:
                    print("try get room")
                    room = Room.objects.get(RoomName=split[1])
                    print("done!")
                    print(room)
                    # room_example.append((conn, str(addr[3])))
                    # print("appending to list!")
                except:
                    print("gagal room")
            # Send message group chat
            elif (message[:7] == '<group>'):

                print("message!" +message)
                message_to_send = addr[2] + ':' + message[7:]
                sender_id = str(addr[3])
                print (addr[2] + ': ' + message[7:])
                # Code broadcast dengan room id disini
                
                # broadcast dengan room dummy
                broadcast(message_to_send, conn, sender_id)
                # db disini
                print("simpan ke db")
                print("ini room " + str(room))
                msg_user = User.objects.get(pk=addr[3])
                
                print("ini user " + str(msg_user))
                try:
                    msg_db = Message.objects.create(room=room,msg=message[7:],AccSent=msg_user,getTime=datetime.datetime.now())
                    print('success')
                except:
                    print('error')


            # create rooom 
            elif (message[:8] == '<create>'):
                split = message.split(',')
                print('masuk create')

                # code create room di DB disini
                room = Room(RoomName=split[1])
                room.save()

                # print('Room Created with ID ' + split[1]) 
                memb = int(addr[3])
                member = User.objects.get(pk=memb)
                # print(member.username)
                roomMemb = Room_Acc.objects.create(AccID=member, RoomID=room)

                
                # Room dummy untuk testing awal
                room_example.append((conn, str(addr[3])))
                print('Room Created with ID ' + split[1])
                print (room_example)

            # invite to group
            elif (message[:8] == '<invite>'):
                print('masuk invite')
                split = message.split(' ')
                invite_id = split[1][:1]

                for client in list_of_clients:
                    if (client[1] == invite_id):
                        print("Receiver ID: " + client[1])
                        client_conn = client[0]
                        try :
                            inv1 = User.objects.get(pk=int(invite_id))
                            # print(inv1.id)
                            inv_data = Room_Acc.objects.create(AccID=inv1, RoomID=room)
                            print(client_conn)
                        except :
                            print('error')

                # room_example.append((client_conn, invite_id)) 
                # print (room_example)

            elif (message[:9] == '<history>'):
                split = message.split(' ')
                print("requested history!")
                print(split[1])#ini id group
                room = Room.objects.get(id='7')
                print("room didapat")
                print(str(room))
                history_pesan=" "
                try:
                    pesan = Message.objects.filter(room=room)
                    
                    for messg in pesan:
                        sender = str(messg.AccSent)
                        history_pesan+= sender+": " + str(messg.msg) + "\n"
                    if(pesan): history_pesan = history_pesan[:-1]
                    conn.send(history_pesan.encode())
                except:
                    conn.send(history_pesan.encode())
                room_example.append((conn, str(addr[3])))

            # Send message personal chat
            elif (message[:10] == '<personal>'):
                print (addr[2] + ': ' + message[10])
                message_to_send = addr[2] + ': ' + message[10:]
                personal_chat(message_to_send, conn, addr[3], unique_id)
                # db disini
            elif (message[:10] == '<roomlist>'):
                split = message.split(' ')
                print("requested list room seorang user!!")
                print(split[1])#ini id group
                try:
                    rooms = Room_Acc.objects.filter(AccID=split[1])
                    print("list room seorang user didapat")
                    print(str(rooms))
                    list_room=" "
                    try:
                        for messg in rooms:
                            list_room+= str(messg.RoomID) + "\n"
                        conn.send(list_room.encode())
                    except:
                        print("gagal!")
                        conn.send(list_room.encode())
                except:
                    print("gagal!")
                    conn.send(list_room.encode())
            else:
                remove(conn)
        except:
            print("error in the thread! continuing")
            break

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
    print("broadcasting!")
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
    
    print("creating Thread")
    threading.Thread(target=clientthread, args=(conn, addr,list_of_clients)).start()

conn.close()