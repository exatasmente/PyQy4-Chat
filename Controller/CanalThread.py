import select,sys
from PyQt4 import QtCore

class CanalThead(QtCore.QObject):
  signalStatus = QtCore.pyqtSignal(list)

  def __init__(self,cliente, parent=None):
    self.cliente = cliente
    super(self.__class__, self).__init__(parent)


  def start(self):
      print(self.cliente.name)
      try:
          socklist = [sys.stdin, self.cliente.socket]

          post = '//listar'
          print(post)
          self.cliente.post(post.encode())
          self.listar(socklist)

      except Exception as e:
          print(e)
          self.cliente.disconnect()

      except KeyboardInterrupt as e:
          self.cliente.disconnect()


  def listar(self,s):
      for sock in s:
          if sock == self.cliente.socket:
              data = self.cliente.getData(sock)
              if data:

                  if data.find('§lista§') > -1:

                      self.isComand(data)


  @QtCore.pyqtSlot()
  def isComand(self,data):
      self.signalStatus.emit(data.split(' '))
