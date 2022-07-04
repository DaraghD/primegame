import socket
import time

def construct_socket():
    print("Welcome to primegame server!")

    host = input("IP: ")
    port = 55555

    scores = {}

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    return s


