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
            # fermer le serveur et la connéxion au client
            server_socket.close()
            socket_client.close()
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
            # fermer le serveur
            server_socket.close()
            exit(0)

        # afficher le message du client
        print(f">{message}\n>", end="")

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host: str = "localhost"

# insérer le port
port: int = 4242


# utiliser la méthode 'bind' pour lier la socket à l'ip et au port
server_socket.bind((host, port))

# utiliser la methode 'listen' pour écouter toutes les nouvelles tentatives de connection
server_socket.listen(1)

# afficher votre ip est sur quel port vous écouter
print(f"host: {host}, port: {port}")

# utiliser la methode 'accept' pour accepter les futurs connection
socket_client, addresse_client = server_socket.accept()

# créer les deux threads 'envoi' pour envoyer et 'recep' pour recevoir
envoi = Thread(target=send, args=[socket_client])
recep = Thread(target=Reception, args=[socket_client])

# lancer les deux threads avec la méthode
envoi.start()
recep.start()

# attendre les messages
envoi.join()
recep.join()

# close les serveurs
server_socket.close()
socket_client.close()




