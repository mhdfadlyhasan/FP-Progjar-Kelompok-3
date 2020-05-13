import socket
import select
import sys
import msvcrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8081
username = input("Please enter your username: ")
server.connect((ip_address, port))
server.send(username.encode())

while True:
    sockets_list = [sys.stdin, server]

    ready_to_read = select.select([server], [], [], 1)[0]
    assert all(server.fileno() != -1 for server in ready_to_read)
    if msvcrt.kbhit(): ready_to_read.append(sys.stdin)
    # read_socket, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in ready_to_read:
        if socks == server:
                message = socks.recv(2048).decode()
                print(message[:-1])
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.flush()

server.close()

