import socket
import pickle
from collections import Counter
import time

def display_scoreboard(data):
    k = Counter(data)# lol
    leaderboard = k.most_common(100)  # returns dictionary with highest values up to n
    # prints keys values
    print("Scoreboard:")
    for i in leaderboard:
        print(i[0], " :", i[1], " ")
    
    print("Thanks for playing, https://github.com/DaraghD/primegame") 
    input(":") 
        
def update_and_recieve_scoreboard(score):
    host = "93.107.167.34"
    port = 55555

    name = input(str("\nEnter nickname: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[CONNECTED]\n")
    message = s.recv(1024).decode()
    if message == "name":
        s.send(name.encode())
            
    message = s.recv(1024).decode()
    if message == "score":
        score = str(score)
        s.send(score.encode())

    s.send("pickle".encode())
    scores = s.recv(12288)
    data = pickle.loads(scores)
    return data

def recieve_scoreboard():
    host = "93.107.167.34"
    port = 55555
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("[CONNECTED]\n")
    s.send("req".encode())
    data = s.recv(12288)
    data = pickle.loads(data)
    return data
