import asyncio
from PyQt4 import QtGui, QtCore


from PyQt4.QtCore import QThreadPool


from Controller import  CanalThread
from Controller.CanalThread import CanalThead
from View import CanalUi
from View.CriarCanal import CriarCanal
from View.ListaCanaisUi import Ui_ListaCanais


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






class ListaCanais(QtGui.QMainWindow,Ui_ListaCanais):
    signalStatus = QtCore.pyqtSignal(list)

    def __init__(self,cliente,parentApp, parent=None):
        self.listaCanais = list()
        self.cliente = cliente
        super(ListaCanais, self).__init__(parent)
        self.parentApp = parentApp
        self.windows = list()
        self.setupUi(self)

        self.criarCanalBtn.clicked.connect(self.criarCanal)
        self.get_thread = CanalThead(self.cliente)

        self.connect(self.get_thread, QtCore.SIGNAL("updateStatus(QString)"), self.updateStatus)

        self.get_thread.start()
        self.cliente.post(str('//listar').encode())

    def criarCanal(self):
        win = CriarCanal(self.cliente, self)
        if win not in self.parentApp.parentApp.windows:
            self.parentApp.parentApp.windows.append(win)
            win.show()
        elif win in self.parentApp.parentApp.windows:
            for w in self.windows:
                if win == w and w.isVisible():
                    w.show()
                    break


    def entrarCanal(self):
        canal = self.sender().objectName().split(' ')
        print(canal[1])
        win = CanalUi.Canal(self.cliente,self,canal[1])
        if win not in self.windows:
            self.windows.append(win)
            win.show()
        elif win in self.windows:
            for w in self.windows:
                if win == w and w.isVisible():
                    w.show()
                    break
        self.cliente.post(str('//entrar '+canal[1]).encode())


    def loadCanal(self,canal):
        canalWidget = QtGui.QWidget(self.scrollAreaContainer)
        canalWidget.setMinimumSize(QtCore.QSize(170, 80))
        canalWidget.setMaximumSize(QtCore.QSize(170, 80))
        canalWidget.setObjectName(_fromUtf8("canalWidget"+' '+str(canal)))

        gridLayout_3 = QtGui.QGridLayout(canalWidget)
        gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"+' '+str(canal)))

        CanalBtn = QtGui.QPushButton(canalWidget)
        CanalBtn.setObjectName(_fromUtf8("CanalBtn"+' '+str(canal)))
        CanalBtn.setText('Entrar')
        CanalBtn.clicked.connect(self.entrarCanal)
        gridLayout_3.addWidget(CanalBtn, 1, 0, 1, 1)

        nomeCanalLabel = QtGui.QLabel(canalWidget)
        nomeCanalLabel.setObjectName(_fromUtf8("nomeCanalLabel"+' '+str(canal)))
        nomeCanalLabel.setText('Canal: '+canal)
        gridLayout_3.addWidget(nomeCanalLabel, 0, 0, 1, 1)
        canalWidget.raise_()
        return canalWidget


    def updateStatus(self, l):
        lista = l.split(' ')
        if lista[0] == '§lista§':
            for canal in lista[1:]:
                if canal not in self.listaCanais:
                    print(canal)
                    self.verticalLayout.addWidget(self.loadCanal(canal))
                    self.listaCanais.append(canal)



