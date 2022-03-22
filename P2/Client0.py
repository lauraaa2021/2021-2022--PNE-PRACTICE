import socket

class Client:
    def __init__(self, ip_client, port_client):
        self.ip = ip_client
        self.port = port_client


    def ping(self):
        print("ok")

    def __str__(self):
        return "Connection to SERVER at" + self.ip + "PORT:" + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()

        return response



