import socket

HOST = '192.168.0.103' #netstat
# HOST = socket.gethostname()  #netstat
PORT = 49648       
 
server_socket=socket.socket()
server_socket.bind((HOST,PORT))
server_socket.listen()
client_socket,addr = server_socket.accept()
print("Message received from", addr)
while True:
    data=client_socket.recv(1024)
    print("Message received from server", data.decode())



