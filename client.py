##
## EPITECH
## ChatPy
## File description:
## Client side
##

from threading import Thread
import socket

Host = "192.168.1.14"
Port = 4242

server_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_client.connect((Host,Port))

print(f"Connecté au serveur{Host} sur le port {Port}")
def Send(server_client):
    while True:
        print(">", end="")
        server_client.send(input().encode('utf8'))
def Reception(server_client):
    while True:
        req = server_client.recv(5000).decode('utf8')
        print(f">{req}")

envoi = Thread(target=Send,args=[server_client])
recep = Thread(target=Reception,args=[server_client])
envoi.start()
recep.start()

envoi.join()
recep.join()