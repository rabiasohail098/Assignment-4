# import socket
# from _thread import *
# import sys


# server = "192.168.100.23"
# port = 5555

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)


# s.listen(2)  
# print("Waiting for a connection, Server Started")

        
# def read_pos(str):
#     str = str.split(",")
#     return (int(str[0]), int(str[1]))

# def make_pos(top):
#     return str(top[0]) + "," + str(top[1])

# pos = [(0, 0), (100, 100)]

# def threaded_client(conn,player):
#     conn.send(str.encode(make_pos(pos[player])))
#     reply = ""
#     while True:
#         try:
#             data = read_pos(conn.recv(2048).decode())
#             pos[player] = data
            
#             if not data:
#                 print("Disconnected")
#                 break
#             else:
#                 if player == 1:
#                     reply = pos[0]
#                 else:
#                     reply = pos[1]
#                 print("Received: ", data)
#                 print("Sending: ", reply)
                
#             conn.send(str.encode(make_pos(reply)))            
#         except:
#             break
#     print("Lost connection")
#     conn.close()
    
    
# currentplayer = 0
# while True:
#     conn, addr = s.accept()
#     print("Connected to: ", addr)
    
#     start_new_thread(threaded_client, (conn,currentplayer))
#     currentplayer += 1

import socket
from _thread import *
import sys

server = "192.168.100.23"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

def read_pos(data):
    data = data.split(",")
    return (int(data[0]), int(data[1]))

def make_pos(pos):
    return str(pos[0]) + "," + str(pos[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = pos[1 - player]
                print("Received:", data)
                print("Sending:", reply)

            conn.send(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if currentPlayer > 1:
        print("Max players reached")
        break
    