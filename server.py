import socket
from _thread import *
import sys
import random

server = "192.168.164.124"  #ip adress we need to put in
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#blackbox

#there is a chance that the port 5555 is taken so we need to add try so it will not crush
try:
    s.bind((server, port))
except socket.error as e: #if there is an error we will see e
    str(e)

s.listen(2) #limit for 2 ppl
print("Waiting for a connection, Server Started")

def read_pos(str:str):
    if str == "reset":
        return "reset"
    str = str.split("_")
    return int(str[0]), int(str[1]), str[2], eval(str[3]), int(str[4])

def make_pos(tup):
    if tup == "reset":
        return "reset"
    return str(tup[0]) + "_" + str(tup[1]) + "_" + str(tup[2]) + "_" + str(tup[3]) + "_" + str(tup[4])

cris_pos = [
    [[
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550)
    ],[
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
    ]],
    [[
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550),
        random.randint(50, 1550)
    ],[
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
        random.randint(50, 630),
    ]]
]
scroll = 0
pos = [(11,634, "Idle", cris_pos[0], scroll), (11,634, "Idle", cris_pos[1], scroll)]
reset_pos = [(11,634, "Idle", cris_pos[0], scroll), (11,634, "Idle", cris_pos[1], scroll)]

def threaded_client(conn, current_player):
    conn.send(str.encode(make_pos(pos[current_player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048*4).decode()) #if thre is an error increas the size

            if not data:
                print("Disconnected")
                break
            else:
                if data == "reset":
                    pos[0] = reset_pos[0]
                    pos[1] = reset_pos[1]
                    continue
                else:
                    if current_player == 1:
                        reply = pos[0]
                    else:
                        reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)
            pos[current_player] = data
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    print("Lost connection")
    conn.close()

current_player = 0
while True:
    conn, addr = s.accept()  #conn = connection addr = addres
    print("Connected to: addr")

    start_new_thread (threaded_client, (conn, current_player))
    current_player += 1