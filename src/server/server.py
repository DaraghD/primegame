import score
import sockets
import threading

def main():
    socket = sockets.construct_socket()
    thread = threading.Thread(target=score.report_scoreboard, args=(socket,))
    thread.start()
    print("here")
    score.handle_scores(socket)

main()
