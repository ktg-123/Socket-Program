import socket
from datetime import datetime

host = '127.0.0.1' #localhost
port = 64000 
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
AF_INET is an address family that is used to designate the 
type of addresses that the socket can communicate with 
(in this case, Internet Protocol v4 addresses).

SOCK_STREAM: TCP socket
SOCK_DGRAM: UDP socket
"""

sock.bind((host, port))
sock.listen(3) # max no of connections = 3

print(f"Server started at {datetime.now()}")

client, addr = sock.accept()

while True:
        recv_message = client.recv(max_size)
        print(f"[{datetime.now()}] Client: {recv_message.decode('utf-8')}")

        if recv_message.decode('utf-8') == 'Bye':
            """
            Message to terminate connection
            """

            break
        msg = input("Enter the message to send to client- ")
        client.send(msg.encode('utf-8'))
        if msg == 'Bye':
            break

client.close()
sock.close()
