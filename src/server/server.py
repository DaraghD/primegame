import score
import sockets

def main():
    socket = sockets.construct_socket()
    score.handle_scores(socket)

main()
