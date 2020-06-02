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
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from chat.models import *
from django.contrib.auth import authenticate

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
    split = packet.split(',')

    # Autentikasi login
    username = split[0]
    password = split[1]
    userf = authenticate(username=username, password=password, is_active = True)
    
    # Jika tidak ditemukan
    if userf is None:
        print ('User not found')
        conn.send("-1".encode())
        clientthread(conn, addr, list_of_clients)

    else:
        conn.send(str(userf.id).encode())

        # Menambahkan username dan id ke addr
        temp = list(addr)
        temp.append(username)
        temp.append(userf.id)
        addr = tuple(temp)

        # Register ID yang sedang online
        list_of_clients.append((conn, str(addr[3]))) 
        print (str(addr[2]) + ' has logged in with ID ' + str(addr[3]))
    
        room = 0
        while True:
            
            message = conn.recv(2048).decode()
            print('Message received')

            # Send message group chat
            if (message[:7] == '<chats>'):
                
                # Message yang akan di send
                message_to_send = addr[2] + ':' + message[7:]
                sender_id = str(addr[3])
                
                # Broadcast
                broadcast(message_to_send, conn, sender_id,room.id)
                msg_user = User.objects.get(pk=addr[3])
                
                # Menaruh message di DB
                try:
                    msg_db = Message.objects.create(room=room,msg=message[7:],AccSent=msg_user,getTime=datetime.datetime.now())
                    print('Message added to DB')
                except:
                    print('Error occurred')

            # Create room 
            elif (message[:8] == '<create>'):
                split = message.split(',')
                print('Creating a group...')

                # Create room di DB
                room = Room(RoomName=split[1])
                room.save()

                # Menambahkan user ke dalam member
                memb = int(addr[3])
                member = User.objects.get(pk=memb)
                roomMemb = Room_Acc.objects.create(AccID=member, RoomID=room)

                print('Group Created with name ' + split[1])

                # room_example.append((conn, str(addr[3])))

            # Create personal chat
            elif (message[:16] == '<createpersonal>'):
                split = message.split(',')

                # Melakukan create room dan menginvite user yang akan dichat
                try:
                    comm, engage_id, invited_id = split[0], addr[3], split[1]
                    engaging_user = User.objects.get(pk=engage_id)
                    invited_user = User.objects.get(pk=invited_id)
                    room = Room(RoomName=engaging_user.username + ' - ' + invited_user.username)
                    room.save()

                    engage = Room_Acc(AccID=engaging_user, RoomID=room).save()
                    print('Personal chat room created with name ' + engaging_user.username + ' - ' + invited_user.username)

                    invite = Room_Acc(AccID=invited_user, RoomID=room).save()
                    print(invited_user.username + ' successfully invited')

                    conn.send(('<personalroomid>,' + str(room.pk)).encode())
                except :
                    print("Error when creating personal chat room") 

            # Melakukan invite ke group
            elif (message[:8] == '<invite>'):
                print('Inviting...')
                split = message.split(' ')
                invite_id = split[1]

                # Mencari user 
                for client in list_of_clients:
                    print(str(client[1]))
                    # Jika online
                    if (str(client[1]) == str(invite_id)):
                        print("Receiver ID: " + client[1])
                        client_conn = client[0]

                        try :
                            inv1 = User.objects.get(pk=int(invite_id))
                            Room_Acc.objects.create(AccID=inv1, RoomID=room)
                            print('User invited to the group')
                        except :
                            print('Error occurred when inviting')

                # room_example.append((client_conn, invite_id)) 

            # Menampilkan history
            elif (message[:9] == '<history>'):
                split = message.split(' ')
                print("Chat history requested...")
                room = Room.objects.get(id=split[1])
                history_pesan=""

                try:
                    pesan = Message.objects.filter(room=room)
                    
                    for messg in pesan:
                        sender = str(messg.AccSent)
                        history_pesan+= sender+":" + str(messg.msg) + "\n"
                    if(pesan): history_pesan = history_pesan[:-1]
                    else: conn.send("Begin your chat now!".encode())
                    conn.send(history_pesan.encode())

                except:
                    conn.send(history_pesan.encode())

                if((conn, str(addr[3])) not in room_example):
                    room_example.append((conn, str(addr[3])))
            
            # Mendapatkan room list
            elif (message[:10] == '<roomlist>'):
                split = message.split(' ')
                print("Room list requested...")

                # Mendapatkan room list
                try:
                    rooms = Room_Acc.objects.filter(AccID=userf.id)
                    
                    list_room=""
                    if(rooms):
                        for messg in rooms:
                            print(messg.RoomID.RoomName)
                            list_room+= str(messg.RoomID.id)+str(". " + messg.RoomID.RoomName) + ","
                        conn.send(list_room.encode())
                        print("Room list sent")
                    else:
                        conn.send("Empty!".encode())

                except:
                    print("Error occurred when trying to get room list for a user")
                    conn.send(list_room.encode())

            # Request room member
            elif (message[:8] == '<member>'):
                split = message.split(' ')
                roomid = int(split[1])

                # Mendapatkan member dari suatu room
                room = Room.objects.get(pk=roomid)
                members = Room_Acc.objects.filter(RoomID=room)
                member_list = ''

                for member in members:
                    member_list += member.AccID.username + ','
                
                conn.send(member_list.encode())

            else:
                print("Empty message")
                remove(conn)

# Function broadcast message
def broadcast(message, connection, sender_id,room_id):
    
    for clients, unique_id in room_example:
        if unique_id != sender_id:
            try:
                clients.send(((message) + "<idroom>" + str(room_id)).encode())
                print("Broadcasted to " + str(room_id))
            except:
                print("Failed to broadcast!")
                clients.close()
                remove(clients)

# Function remove
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
    
    if connection in room_example:
        room_example.remove(connection)

while True:
    # Accept dari client
    conn, addr = server.accept()
    
    # Membuat Thread
    print("Creating Thread")
    threading.Thread(target=clientthread, args=(conn, addr,list_of_clients)).start()

conn.close()