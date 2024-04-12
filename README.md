
# ChatPy - Coding Club EPITECH

Le but de ce Coding club est de réaliser une messagerie entre deux machines.



## Documentation

 - [Les Bases en Python](https://courspython.com/bases-python.html)
 - [Les Sockets en Python](https://docs.python.org/fr/3/howto/sockets.html)
 - [Les addresses IP](https://www.it-connect.fr/les-adresses-ip-pour-les-debutants/)


## Les Sockets en Python

Les sockets en Python permettent la communication bidirectionnelle entre des processus sur différentes machines ou sur la même machine via un réseau. Ils peuvent utiliser différents protocoles, tels que TCP ou UDP, pour la transmission de données.






### Exemple

```python
import socket

# Créer un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse et au port
server_socket.bind(("localhost", 4242))

# Mettre en écoute sur le port
server_socket.listen(1)

# Accepter les connexions entrantes
client_socket, client_address = server_socket.accept()
```
## Les addresses IP
Les adresses IP sont des identifiants uniques attribués à chaque appareil connecté à un réseau. Elles sont utilisées pour identifier l'emplacement d'un appareil sur un réseau et permettent la communication entre les appareils.

### Exemple

```bash
>> hostname -I
192.168.0.1
```
## Serveur et Client

Dans une architecture client-serveur, le serveur écoute les connexions entrantes des clients et fournit des services en réponse à leurs demandes. Les clients initient des connexions vers le serveur pour accéder à ces services.

### Exemple de serveur en Python

```python
import socket

# Créer un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à l'adresse et au port
server_socket.bind(("localhost", 4242))

# Mettre en écoute sur le port
server_socket.listen(1)

# Accepter les connexions entrantes
client_socket, client_address = server_socket.accept()
```

### Exemple de client en Python

```python
import socket

# Créer un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur
client_socket.connect(("localhost", 4242))
```

## Les Ports

Les ports sont des numéros de 16 bits qui identifient un processus sur un hôte. Ils sont utilisés pour diriger le trafic réseau vers des applications spécifiques.

```python
port = 4242
```

## Les Threads en Python

Les threads sont des processus légers qui permettent l'exécution simultanée de plusieurs tâches. Ils sont utiles pour gérer les communications réseau concurrentes.

### Exemple d'utilisation des threads
```python
from threading import Thread

# Fonction à exécuter dans un thread
def handle_client(client_socket):
    # Logique de traitement des données du client
    pass

# Créer et démarrer un thread
client_thread = Thread(target=handle_client, args=(client_socket,))
client_thread.start()
```
