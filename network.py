import socket

class Network:
    def __init__(self):
        self.client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.27" #need to be the same number from the server!!!
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
    
    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
