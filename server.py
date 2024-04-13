##
## EPITECH
## ChatPy
## File description:
## Server side
##

from threading import Thread
import socket

def Send(client):
    while True:
        print(">", end="")
        client.send(input().encode('utf8'))
def Reception(client):
    while True:
        req = client.recv(5000).decode('utf8')
        if not req:
            break
        print(f">{req}\n>", end="")

Host = "localhost"
Port = 3000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((Host,Port))
server.listen(1)

print("On attend des connexions")
client, addrs = server.accept()
print("Client Connecté")
envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])
recep.start()
envoi.start()

recep.join()
envoi.join()

server.close
client.close


