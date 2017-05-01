import socket, select, sys
import asyncio

class Cliente:
    def __init__(self, nome):
        self.host = '127.0.0.1'
        self.port = 7000
        self.name = nome

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def prompt(self):
        sys.stdout.write('')
        sys.stdout.flush()

    def getData(self, s):
        try:
            data = s.recv(4096).decode()
            return data

        except Exception as e:
            print(e)
            self.disconnect()
            pass

    def disconnect(self):
        self.socket.send(str("|sair|").encode())
        self.socket.close()
        sys.exit()

    async def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            self.socket.send(self.name.encode())

        except:
            return False


        return True

    def post(self, msg):
        print(msg)
        self.socket.send(msg)

