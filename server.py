import socket
from _thread import *
import sys

server = "10.0.0.27"  #ip adress we need to put in
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
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,634), (0,634)]

def threaded_client(conn, current_player):
    conn.send(str.encode(make_pos(pos[current_player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode()) #if thre is an error increas the size
            pos[current_player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if current_player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)
            
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