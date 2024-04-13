import socket
import os
from threading import Thread

def send(client):
    while True:
        # affiche le prompt
        print(">", end="")

        #utiliser la méthode input pour récupérer le message de l'utilisateur
        message: str = ...

        #ustiliser la méthode send avec 'message' pour envoyer un message au client
        client.send(message.encode("utf-8"))

        if message == 'exit':
            print("[ATTENTION] déconnexion en cours...")
            # fermer le serveur et la connéxion au client
            ...
            ...
            exit(0)

def Reception(client):

    while True:
        # récupérer le message du client
        message: str = ...

        # si jamais il n y'a pas de réponse on quitte la focntion
        if not message:
            break

        if message == 'exit':
            print("[ATTENTION] connéxion rompue")
            # fermer le serveur
            ...
            exit(0)

        # afficher le message du client
        print(f">{message}\n>", end="")

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host = ...

# insérer le port
port = ...


# utiliser la méthode 'bind' pour lier la socket à l'ip et au port
server_socket.bind((host, port))

# utiliser la methode 'listen' pour écouter toutes les nouvelles tentatives de connection
server_socket.listen(1)

# afficher votre ip est sur quel port vous écouter
print(f"host: {host}, port: {port}")

# utiliser la methode 'accept' pour accepter les futurs connection
# indice utiliser la fonction fileno
host_client, addresse_client = server_socket.accept()

# créer les deux threads 'envoi' pour envoyer et 'recep' pour recevoir
envoi = ...
recep = ...


# lancer les deux threads avec la méthode
envoi.start()
...

# attendre les messages
envoi.join()
...

# close les serveurs
server_socket.close()
host_client.close()

