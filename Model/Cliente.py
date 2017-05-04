import socket, select, sys
import asyncio

class Cliente:
    def __init__(self, nome):
        self.host = '127.0.0.1'
        self.port = 50000
        self.name = nome

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)




    def getData(self):
        try:

            data = self.socket.recv(4000).decode()
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
          Con = self.socket.connect_ex((self.host, self.port))

          if Con == 0:
              self.socket.send(self.name.encode())
              return True
          else:
              return False


    def post(self, msg):

        try:
            self.socket.send(msg)
        except Exception as e:
            sys.exit()


