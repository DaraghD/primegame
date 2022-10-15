import game
import menu
import scoreboard
import os

done = False

def main():
    selection = menu.main_menu()
    if selection == "1":
        game.run()
    if selection == "2":
        data = scoreboard.recieve_scoreboard()
        scoreboard.display_scoreboard(data)
    if selection == "3":
        print("just enter a prime lol")

        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    if selection == "4":
        exit(0)

while True:
    main()
