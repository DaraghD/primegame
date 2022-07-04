import game
import menu
import scoreboard

def main():
    selection = menu.main_menu()
    if selection == "1":
        game.run()
    if selection == "2":
        data = scoreboard.recieve_scoreboard()
        scoreboard.display_scoreboard(data)


main()
