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

def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048) #if thre is an error increas the size
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept()  #conn = connection addr = addres
    print("Connected to: addr")

    start_new_thread (threaded_client, (conn,)) 