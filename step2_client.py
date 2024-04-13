import socket
from os import write
from threading import Thread


def send(server):

    while True:
        # affiche le prompt
        print(">", end="")

        #utiliser la méthode input pour récupérer le message de l'utilisateur
        message: str = ...

        #ustiliser la méthode send avec 'message' pour envoyer un message au client
        ...

        if message == 'exit':
            print("[ATTENTION] déconnéxion...")
            exit(0)

def Reception(server):

    while True:
        # récupérer le message du client
        message: str = ...

        # si jamais il n y'a pas de réponse on quitte la focntion
        if not message:
            break

        #si mon interlocuteru exit je dois quitter le server aussi
        if message == 'exit':
            print("[ATTENTION] connéxion rompue par le serveur")
            exit(0)

        # afficher le message du client
        print(f">{message}\n>", end="")

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host = ...

# insérer le port
port = ...

# utiliser la méthode 'connect' de server_socket pour se connecter au serveur
server_socket.connect((host, port))

# afficher votre ip est sur quel port vous écouter
print(f"host: {host}, port: {port}")

# créer les deux threads 'envoi' pour envoyer et 'recep' pour recevoir
envoi = ...
recep = ...

# lancer les deux threads avec la méthode
envoi.start()
...

# attendre les messages
envoi.join()
...

server_socket.close()

