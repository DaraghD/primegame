import pickle

scores = {}

def handle_scores(s):
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

def report_scoreboard(s):
     while True:
        conn, addr = s.accept()

        print(scores)
        data = pickle.dumps(scores)

        message = conn.recv(1024)
        if message.decode() == "req":
            conn.send(data)

