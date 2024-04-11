#!usr/bin/env python3
##
## EPITECH PROJECT, 2024
## my_navy_python
## File description:
## navy
##

import socket
import os
import linecache

PORT = 4242

MAP_PLAYER1: list[str] = [
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
]

MAP_PLAYER2: list[str] = [
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
    "........",
]


def print_map(map: list[str]) -> None:
    print(" | A B C D E F G H ")
    print("-+-----------------")
    for i in range(0, len(map)):
        print(f"{i + 1}|", end="")
        for c in map[i]:
            print(f" {c}", end="")
        print()

def main(port: int) -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"host: {socket.gethostbyname('localhost')} port: {port}")
    print("Waiting for connections...")
    (client_socket, addr) = server_socket.accept()
    print("Connected !")
    print(f"client host: {client_socket.getsockname()[0]}")
    client_fd: int = client_socket.fileno()
    host_fd: int = server_socket.fileno()
    os.write(client_fd, bytes("Hello from server !\n".encode("utf-8")))
    os.write(client_fd, bytes("$>".encode("utf-8")))
    msg = linecache.getline(lineno=client_fd)
    print(msg)
main(4242)