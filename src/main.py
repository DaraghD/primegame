import game
import menu
import scoreboard
import time



def main():
    selection = menu.main_menu()
    if selection == "1":
        game.run()
    if selection == "2":
        data = scoreboard.recieve_scoreboard()
        scoreboard.display_scoreboard(data)
    if selection == "3":
        print("just enter a prime lol")
        for i in range(10):
            print("\n")

while True:
    main()
