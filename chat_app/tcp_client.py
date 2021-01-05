import socket
from datetime import datetime

host = '127.0.0.1'
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

sock.connect((host, port))

print(f"Client started at {datetime.now()}")

while True:
    send_message = input("Enter a message for server- ")
    sock.send(send_message.encode('utf-8'))
    if send_message == "Bye":
        break
    recv_message = sock.recv(max_size)
    
    print(f"[{datetime.now()}] Server: {recv_message.decode('utf-8')}")

    if recv_message.decode('utf-8') == 'Bye':
        """
        Message to terminate connection
        """

        break

sock.close()

