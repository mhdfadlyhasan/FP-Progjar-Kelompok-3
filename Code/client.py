import socket
import select
import sys
import msvcrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8081

# Input username & ID sendiri
username = input("Please enter your username: ")
your_id = input("Please enter your ID: ")
server.connect((ip_address, port))

# Send username + id
packet = username + ',' + your_id
server.send(packet.encode())

# Input id orang yang ingin di chat
personal_id = input("Please enter the person's ID: ")
personal = '<id>' + personal_id
# print(personal)
server.send(personal.encode())

while True:
    sockets_list = [sys.stdin, server]

    # Tunggu input
    ready_to_read = select.select([server], [], [], 0.01)[0]#delay diperkecil biar lebih responsive
    assert all(server.fileno() != -1 for server in ready_to_read)
    if msvcrt.kbhit(): ready_to_read.append(sys.stdin)

    
    for socks in ready_to_read:
        # Terima message
        if socks == server:
                message = socks.recv(2048).decode()
                print(message[:-1])
        # Send message
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.flush()

server.close()

