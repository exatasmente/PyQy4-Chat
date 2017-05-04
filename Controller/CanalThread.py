import  asyncio

from PyQt4.QtCore import SIGNAL, QThread


class CanalThread(QThread):

      def __init__(self,cliente):
          QThread.__init__(self)
          self.cliente = cliente
          self.erroList = [("§Error02§","erro02(QString)"),("§Error03§","erro03(QString)"),
                           ("§Error04§","erro04(QString)"),("§Error05§","erro05(QString)")]


      def run(self):
          while 1:
              data = self.cliente.getData()


              if data:

                 if data.__contains__("§")==False:
                     r = data.split(':')
                     self.emit(SIGNAL('updateStatus(QString,QString)'), r[0],r[1])

                 elif data.__contains__("§"):

                     r = data.split(":")

                     if data.find("§lista§")>-1:
                         self.emit(SIGNAL('listaUpdate(QString)'),r)

                     else:
                         error = [ i for i in self.erroList if i[0] == r[0]]

                         if error:
                             self.emit(SIGNAL(error[0][1]), r[1])


      def __del__(self):

          self.wait()