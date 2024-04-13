import socket
import os
from threading import Thread

def send(client: socket.socket):
    while True:
        # affiche le prompt
        print(">", end="")

        #utiliser la méthode input pour récupérer le message de l'utilisateur
        message: str = input()

        #ustiliser la méthode send avec 'message' pour envoyer un message au client
        client.send(message.encode("utf-8"))

        if message == 'exit':
            print("[ATTENTION] déconnexion")
            exit(0)

def Reception(client: socket.socket):

    while True:
        # récupérer le message du client
        message: str = client.recv(1024).decode("utf-8")

        # si jamais il n y'a pas de réponse on quitte la focntion
        if not message:
            break

        if message == 'exit':
            print("[ATTENTION] connexion rompue")
            exit(0)

        # afficher le message du client
        print(f">{message}\n>", end="")

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host: str = "localhost"

# insérer le port
port: int = 4242

server_socket.connect((host, port))

print(f"host: {host}, port: {port}")

# créer les deux threads 'envoi' pour envoyer et 'recep' pour recevoir
envoi = Thread(target=send, args=[server_socket])
recep = Thread(target=Reception, args=[server_socket])

# lancer les deux threads avec la méthode
envoi.start()
recep.start()

# attendre les messages
envoi.join()
recep.join()

