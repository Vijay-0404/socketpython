import socket

c = socket.socket()

c.connect((' 192.168.202.202',4000))

c.recv(1024)
