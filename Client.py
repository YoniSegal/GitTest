import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '172.19.3.151'
dest_port = 5400
s.connect((dest_ip, dest_port))
msg = input("Message to send: ")
while not msg == 'quit':
    s.send(msg.encode())
    data = s.recv(4096)
    print("Server sent: ", data.decode())
    msg = input("Message to send: ")
s.close()

