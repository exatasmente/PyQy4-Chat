import sys
import asyncio
from View import  ListaCanais
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import *

from Model import Cliente
from View import GUI


class App(QApplication):
    def __init__(self,argv = None):
        super(App, self).__init__(argv)
        self.windows = list()
        win = Window(self)
        win.show()
        self.windows.append(win)

class Window(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parentApp, parent=None):
        super(Window, self).__init__(parent)
        self.parentApp = parentApp
        self.setupUi(self)
        self.EntrarBtn.clicked.connect(self.login)
        self.EntrarBtn.setShortcut(QtCore.Qt.Key_Return)

    def login(self):
        if self.loginField.text():
            cliente = Cliente.Cliente(self.loginField.text())
            COM = False
            loop = asyncio.get_event_loop()
            COM = loop.run_until_complete(cliente.connect())


            if COM:

                win = ListaCanais.ListaCanais(cliente, self)
                self.parentApp.windows.pop()
                self.parentApp.windows.append(win)
                win.show()

                self.close()
            else:
                self.alert('Não Foi Possivél Conectar')
        else:
            self.alert('Nome Inválido')



    def alert(self, text):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)

        msg.setText(text)
        msg.setWindowTitle("Atenção!")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)

        retval = msg.exec_()



def main():
    app = App(sys.argv)

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()



