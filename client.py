import socket

c = socket.socket()

c.connect(('localhost',4000))

c.recv(1024)