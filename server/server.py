import socket
import time
import sys
import pickle

print("\nWelcome to primegame server!\n")
print("[LOADING]")
time.sleep(1)

host = "192.168.1.2"
port = 55555

scores = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()


def main():
    while True:
        conn, addr = s.accept()

        conn.send("name".encode())
        name = conn.recv(1024)
        name = name.decode()
        print(name)

        conn.send("score".encode())
        score = conn.recv(1024)
        score = score.decode()
        print(score)
        
        scores[name] = score
        print(scores)
        data = pickle.dumps(scores)

        message = conn.recv(1024)
        if message.decode() == "pickle":
            conn.send(data)





main()


