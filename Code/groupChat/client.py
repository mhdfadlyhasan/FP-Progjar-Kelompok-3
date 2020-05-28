import socket
import select
import sys
# import msvcrt

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

while True:

    # Pilih mode
    print("Type the mode's number that you want to use\n1. Personal Chat\n2. Group Chat\n3. Quit\n")
    mode = input('Mode: ')

    # Personal Chat
    if (mode == '1'):

        # Input id orang yang ingin di chat
        personal_id = input("Please enter the person's ID: ")
        personal = '<id>' + personal_id
        # print(personal)
        server.send(personal.encode())

        while True:
            sockets_list = [sys.stdin, server]

            # Tunggu input
            ready_to_read = select.select([server], [], [], 0.01)[0] #delay diperkecil biar lebih responsive
            assert all(server.fileno() != -1 for server in ready_to_read)
            # if msvcrt.kbhit(): 
            ready_to_read.append(sys.stdin)

            for socks in ready_to_read:
                # Terima message
                if socks == server:
                    message = socks.recv(2048).decode()
                    print(message)

                # Send message
                else:
                    message = sys.stdin.readline()
                    message = '<personal>' + message
                    server.send(message.encode())
                
                sys.stdout.flush()

    # Group Chat
    elif (mode == '2'):

        while True:
            sockets_list = [sys.stdin, server]

            # Tunggu input
            ready_to_read = select.select([server], [], [], 0.01)[0] #delay diperkecil biar lebih responsive
            assert all(server.fileno() != -1 for server in ready_to_read)
            # if msvcrt.kbhit():
            ready_to_read.append(sys.stdin)

            for socks in ready_to_read:
                # Terima message
                if socks == server:
                    message = socks.recv(2048).decode()
                    print(message)

                # Send message
                else:
                    message = sys.stdin.readline()
                    # Format <create> ID_room
                    if (message[:8] == '<create>'):
                        split = message.split(' ')
                        print ('You created a room with ID ' + split[1])
                        server.send(message.encode())

                    # Format <invite> ID_user
                    elif (message[:8] == '<invite>'):
                        split = message.split(' ')
                        print ('You invited user with ID ' + split[1])
                        server.send(message.encode())   

                    # Format <join> ID_room
                    elif (message[:6] == '<join>'):
                        split = message.split(' ')
                        print ('You joined room with ID ' + split[1])
                        server.send(message.encode())
                        
                    else:
                        message = '<group>' + message
                        # print(message)
                        server.send(message.encode())
                        sys.stdout.flush()
                    
                    sys.stdout.flush()

    # Quit
    elif (mode == '3'):
        message = '<quit>'
        server.send(message.encode())
        server.close()
        sys.exit()

    # Mode Error Handler
    else:
        print('Wrong mode please try again')


