import socket

HOST = '192.168.0.103' #netstat
# HOST = socket.gethostname()  #netstat -a
PORT = 49648       

client_socket=socket.socket()
client_socket.connect((HOST,PORT))
while True:
    print("Enter the message")
    message=input()
    client_socket.sendall(message.encode())
