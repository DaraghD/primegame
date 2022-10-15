import random
import scoreboard
import functions

def run():

    score = 0
    print("prime number: a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11) ")
    print("hello, you will be given 3 numbers, goal is to make a prime out of them")
    while True:
        # see functions.py
        x = random.randrange(0, 9, 1)
        y = random.randrange(0, 9, 1)
        z = random.randrange(0, 9, 1)
        pt = functions.mPrime(x, y, z)  # prime tuple
        answerlist = functions.ifPrime(pt[0], pt[1], pt[2], pt[3], pt[4], pt[5])

        while len(answerlist) == 0:
            x = random.randrange(0, 9, 1)
            y = random.randrange(0, 9, 1)
            z = random.randrange(0, 9, 1)
            pt = functions.mPrime(x, y, z)
            answerlist = functions.ifPrime(pt[0], pt[1], pt[2], pt[3], pt[4], pt[5])
        if len(answerlist) != 0:
            print("\nHere are your 3 numbers", x, y, z)

        answer = int(input(":"))
        answer_string = str(answer)
        answer_length = len(answer_string)
        if answer in answerlist:
            score += 1
            print("you win, your score is", score)
            print("Possible answers were,", answerlist)

        else:
            print("you lose,your score is", score)
            print("Possible answers were,", answerlist)
            answer = input("Would you like to upload your score? [Y/n] ")
            if answer == "n":
                score = 0
                continue
            else:
                data = scoreboard.update_and_recieve_scoreboard(score)
                scoreboard.display_scoreboard(data)
                break
