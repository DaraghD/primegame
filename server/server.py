import socket
import time
import sys

print("\nWelcome to primegame server!\n")
print("[LOADING]")
time.sleep(1)

host = input("input IP:")
port = 55555

scores = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()


def main():
    while True:
        conn, addr = s.accept()

        conn.send("name".encode())
        name = conn.recv(1024)
        name = name.decode()

        conn.send("score".encode())
        score = conn.recv(1024)
        score = score.decode()
        with open('scores.txt') as f:
            for line in f:
                name, score = line.strip().split()
                scores.append ((name, int(score)))

        # get top 5
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

        print('The First 5 Highscores are:')
        for item in sorted_scores[:5]:
            conn.send(item.encode())




main()


