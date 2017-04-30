from PyQt4 import QtGui, QtCore
from Controller import  CanalThread
from Controller.CanalThread import CanalThead
from View import CanalUi
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

        self.setupUi(self)

        self.worker = CanalThread.CanalThead(cliente)
        self.worker_thread = QtCore.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # Make any cross object connections.
        self._connectSignals()

        self.nomeCliente.setText(self.cliente.name)


    def entrarCanal(self):
        win = CanalUi.Canal(self.cliente, self)
        win.show()
        self.parentApp.parentApp.windows.append(win)


    def loadCanal(self,canal):
        canalWidget = QtGui.QWidget(self.scrollAreaContainer)
        canalWidget.setMinimumSize(QtCore.QSize(170, 80))
        canalWidget.setMaximumSize(QtCore.QSize(170, 80))
        canalWidget.setObjectName(_fromUtf8("canalWidget"))

        gridLayout_3 = QtGui.QGridLayout(canalWidget)
        gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        CanalBtn = QtGui.QPushButton(canalWidget)
        CanalBtn.setObjectName(_fromUtf8("CanalBtn"))
        CanalBtn.setText('Entrar')
        CanalBtn.clicked.connect(self.worker.start)
        gridLayout_3.addWidget(CanalBtn, 1, 0, 1, 1)

        nomeCanalLabel = QtGui.QLabel(canalWidget)
        nomeCanalLabel.setObjectName(_fromUtf8("nomeCanalLabel"))
        nomeCanalLabel.setText('Canal: '+canal)
        gridLayout_3.addWidget(nomeCanalLabel, 0, 0, 1, 1)
        canalWidget.raise_()

        return canalWidget

    @QtCore.pyqtSlot(list)
    def updateStatus(self, lista):
        if lista[0] == '§lista§':
            for canal in lista[1:]:
                if canal not in self.listaCanais:
                    self.verticalLayout.addWidget(self.loadCanal(canal))
                    self.listaCanais.append(canal)


    def _connectSignals(self):
        self.verticalLayout.addWidget(self.loadCanal('Teste'))
        self.signalStatus.connect(self.updateStatus)
        self.worker.signalStatus.connect(self.updateStatus)





    def forceWorkerReset(self):
        if self.worker_thread.isRunning():
            self.worker_thread.terminate()
            self.worker_thread.wait()

            self.worker_thread.start()


    def forceWorkerQuit(self):
         if self.worker_thread.isRunning():
            self.worker_thread.terminate()
            self.worker_thread.wait()
