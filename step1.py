import socket
from os import write

# Création de la socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# insérer l'ip
host = ...

# insérer le port
port = ...


# utiliser la méthode 'bind' pour lier la socket à l'ip et au port
...

# utiliser la methode 'listen' pour écouter toutes les nouvelles tentatives de connection
...

# afficher votre ip est sur quel port vous écouter
...

# utiliser la methode 'accept' pour accepter les futurs connection
# indice utiliser la fonction fileno
host_client, addresse_client = ...


# insérer le message de bienvenue !
message: str = ...

# récuperer le l'entrée du client avec le méthode fileno
entree_client: int = host_client.fileno()

# enfin avec la methode write on écrit notre messeg sur l'entrée du client
write(entree_client, bytes(message.encode("utf-8")))