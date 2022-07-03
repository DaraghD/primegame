import random
import sympy as pm
import socket
import pickle
from collections import Counter
import time



def scoreboard(data):
    k = Counter(data)# lol
    leaderboard = k.most_common(5)  # returns dictionary with highest values up to n
    # prints keys values
    print("Scoreboard:")
    for i in leaderboard:
        print(i[0], " :", i[1], " ")
    
    print("Thanks for playing, https://github.com/DaraghD/primegame") 
    time.sleep(1000000) # stops window from closing immediately 
        
        
def highscore(score):
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
    scoreboard(data)


score = 0 
print("prime number: a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11) ")
print("hello, you will be given 3 numbers, goal is to make a prime out of them")
while True:
    counter = 0
    answerlist = []

    x = random.randrange(0, 9, 1)
    y = random.randrange(0, 9, 1)
    z = random.randrange(0, 9, 1)


    def mPrime(n1, n2, n3):
        global p1, p2, p3, p4, p5, p6
        n1_string = str(n1)
        n2_string = str(n2)
        n3_string = str(n3)
        p1s = n1_string + n2_string + n3_string
        p2s = n1_string + n3_string + n2_string
        p3s = n2_string + n1_string + n3_string
        p4s = n2_string + n3_string + n1_string
        p5s = n3_string + n1_string + n2_string
        p6s = n3_string + n2_string + n1_string
        p1 = int(p1s)
        p2 = int(p2s)
        p3 = int(p3s)
        p4 = int(p4s)
        p5 = int(p5s)
        p6 = int(p6s)


    def ifPrime(n1, n2, n3, n4, n5, n6):
        global counter
        counter = 0
        g1 = pm.isprime(n1)
        if g1 == True:
            counter += 1
            answerlist.append(n1)

        g2 = pm.isprime(n2)
        if g2 == True:
            counter += 1
            answerlist.append(n2)

        g3 = pm.isprime(n3)
        if g3 == True:
            counter += 1
            answerlist.append(n3)

        g4 = pm.isprime(n4)
        if g4 == True:
            counter += 1
            answerlist.append(n4)

        g5 = pm.isprime(n5)
        if g5 == True:
            counter += 1
            answerlist.append(n5)
        g6 = pm.isprime(n6)
        if g6 == True:
            counter += 1
            answerlist.append(n6)


    while counter == 0:
        x = random.randrange(0, 9, 1)
        y = random.randrange(0, 9, 1)
        z = random.randrange(0, 9, 1)
        mPrime(x, y, z)
        ifPrime(p1, p2, p3, p4, p5, p6)
        if counter > 0:
            print("\nHere are your 3 numbers", x, y, z)

    answer = int(input())
    answer_string = str(answer)
    answer_length = len(answer_string)
    if answer in answerlist:
        score += 1
        print("you win, your score is", score)
        print("Possible answers were,", answerlist)

    else:
        print("you lose,your score is", score)
        print("Possible answers were,", answerlist)
        answer = input("Would you like to upload your score [Y/n]")
        if answer == "n":
            continue
        else:
            highscore(score)
            break



