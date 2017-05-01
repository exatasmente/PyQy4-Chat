from PyQt4 import QtGui,QtCore
from time import sleep

from View.CriarCanalUi import Ui_CriarCanal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class CriarCanal(QtGui.QMainWindow,Ui_CriarCanal):

    def __init__(self,cliente,parentApp, parent=None):
        self.listaCanais = list()
        self.cliente = cliente
        super(CriarCanal, self).__init__(parent)
        self.parentApp = parentApp
        self.setupUi(self)
        self.Criar.clicked.connect(self.criarCanal)
        self.Criar.setShortcut("Return")

    def criarCanal(self):
        if self.NomeCanalInput.text():
            if self.NomeCanalInput.text() not in self.parentApp.listaCanais:
                self.cliente.post(str('//criar ' + self.NomeCanalInput.text()).encode())

                self.parentApp.verticalLayout.addWidget(self.parentApp.loadCanal(self.NomeCanalInput.text()))
                self.parentApp.listaCanais.append(self.NomeCanalInput.text())
                self.close()
            else:
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Warning)
                msg.setText('Canal Já Existe ou Inválido')
                msg.setWindowTitle("Atenção!")
                msg.setStandardButtons(QtGui.QMessageBox.Ok)

                retval = msg.exec_()




