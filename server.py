import socket
from _thread import *

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

positions = [(50, 50), (700, 500)]  # Starting positions for players


def read_pos(pos):
    pos = pos.split(",")
    return int(pos[0]), int(pos[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(positions[player])))
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())

            if not data:
                print("Disconnected")
                break

            positions[player] = data

            if player == 1:
                reply = positions[0]
            else:
                reply = positions[1]

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
