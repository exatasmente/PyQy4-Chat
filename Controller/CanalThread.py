

from PyQt4.QtCore import SIGNAL, QThread


class CanalThead(QThread):

      def __init__(self,cliente):
          QThread.__init__(self)
          self.cliente = cliente


      def run(self):

          try:
              sock = self.cliente.socket
              for i in range(1):
                      data = self.cliente.getData(sock)
                      if data:
                          print(data)
                          if data.find('§lista§')>-1:
                              r =data
                              self.emit(SIGNAL('updateStatus(QString)'),r)
                          else:
                               r = data.split(':')
                               print(r)
                               self.emit(SIGNAL('receber(QString,QString)'), r[1], r[0])







          except Exception as e:
              print('EE',e)
              self.cliente.disconnect()

          except KeyboardInterrupt as e:
              self.cliente.disconnect()

      def __del__(self):
          self.wait()