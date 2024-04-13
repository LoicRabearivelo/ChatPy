import socket
from os import write
from threading import Thread


def send(server: socket.socket):

    while True:
        # affiche le prompt
        print(">", end="")

        #utiliser la méthode 'input' pour récupérer le message de l'utilisateur
        message: str = ...

        #ustiliser la méthode 'send' avec 'message' pour envoyer un message au client
        ...

        if message == 'exit':
            print("[ATTENTION] déconnexion...")
            exit(0)

def Reception(server: socket.socket):

    while True:
        # récupérer le message du client avec la méthode 'recv'
        message: str = ...

        # si jamais il n y'a pas de réponse on quitte la focntion
        if not message:
            break

        # mon interlocuteur a quitté le chat je dois donc quitter
        if message == 'exit':
            print("[ATTENTION] connexion rompue par le serveur")
            exit(0)

        # afficher le message du client
        print(f">{message}\n>", end="")

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host: str = ...

# insérer le port
port: int = ...

# utiliser la méthode 'connect' de server_socket pour se connecter au serveur
server_socket.connect((host, port))

# afficher votre ip est sur quel port vous écouter
print(f"host: {host}, port: {port}")

# créer les deux threads 'envoi' pour envoyer et 'recep' pour recevoir
envoi: Thread = ...
recep: Thread = ...

# lancer les deux threads avec la méthode 'start'
...
...

# joindre les threads avec son interlocuteur avec la méthode 'join'
...
...

# fermer le serveur
server_socket.close()

