import socket
from _thread import *
import sys

server = "127.0.0.1"  # LOCAL TESTING — for multiple PCs use your real IP
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Server started, waiting for connections...")

positions = [(100, 100), (300, 300)]

def read_pos(data):
    x, y = data.split(",")
    return int(x), int(y)

def make_pos(pos):
    return f"{pos[0]},{pos[1]}"

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(positions[player])))
    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            positions[player] = read_pos(data)
            other_player = 1 - player
            conn.send(str.encode(make_pos(positions[other_player])))
        except:
            break

    print("Lost connection")
    conn.close()

player_count = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, player_count))
    player_count += 1
