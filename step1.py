import socket
from os import write

# Création de la socket
server_socket: socket.socket = ...

# insérer l'ip
host: str = ...

# insérer le port
port: int = ...


# utiliser la méthode 'bind' pour lier la socket à l'ip et au port
...

# utiliser la methode 'listen' pour écouter toutes les nouvelles tentatives de connection
...

# afficher votre ip est sur quel port vous écouter
...

# utiliser la methode 'accept' pour accepter les futurs connection
# socket_client représente la socket du client
# addresse_client représente son addresse (ip, port)
socket_client, addresse_client = ...


# insérer le message de bienvenue !
message: str = ...

# récuperer le l'entrée du client avec le méthode fileno
entree_client: int = ...

# enfin avec la methode write on écrit notre messeg sur l'entrée du client
write(entree_client, bytes(message.encode("utf-8")))