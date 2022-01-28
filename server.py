import socket

s = socket.socket()
print("socketed was created successfully")
ADDR = (' 192.168.202.202',4000)
s.bind(ADDR)
s.listen(10)
print("waitiing for the connections")

while True:
    c, aadr = s.accept()
    print("connections are connected with", aadr)
    c.send(bytes('hello machan', 'utf-8'))

    c.close()
