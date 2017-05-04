
from View.CanalView import Ui_Canal
from PyQt4 import QtCore, QtGui
from Controller.CanalThread import CanalThread
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



class Canal(QtGui.QMainWindow,Ui_Canal):

    def __init__(self,Cliente, parentApp, nomeCanal,parent= None):
       super(Canal, self).__init__(parent)
       self.setupUi(self)
       self.nomeCanal = nomeCanal
       self.cliente = Cliente
       self.parentApp = parentApp
       self.setWindowTitle(str('Canal ' + str(self.nomeCanal)))
       self.qtMsg = 0
       self.msglist = list()

       self.spacerItem = QtGui.QSpacerItem(100, 70, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
       self.verticalLayout.addItem(self.spacerItem)

       self.pushButton.clicked.connect(self.enviar)
       self.pushButton.setShortcut("Return")

       self.get_thread = self.parentApp.get_thread

       self.connect(self.get_thread, QtCore.SIGNAL("updateStatus(QString,QString)"), self.updateStatus)
       self.connect(self.get_thread, QtCore.SIGNAL("listaUpdate(QString)"), self.listaUpdate)




    def __eq__(self, other):
        if type(other) == type(self):
           return self.nomeCanal == other.nomeCanal
        return False

    def closeEvent(self, event):

        if self.nomeCanal == '0':
            event.accept()


        else:
            msg = '//sair'
            self.cliente.post(msg.encode())
            self.parentApp.canalAberto = None
            event.accept()



    def listaUpdate(self,l):

        self.parentApp.updateStatus(l)


    def newMsg(self, i, msg, nome= None ):
        MsgWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        MsgWidget.setMinimumSize(QtCore.QSize(401, 40))
        MsgWidget.setMaximumSize(QtCore.QSize(401, 40))
        if nome:

            if nome == 'Sistema ':
                MsgWidget.setStyleSheet(_fromUtf8("QWidget{\n"
                                                  "color : #ffffff;\n"
                                                  "border-radius: 10px;\n"
                                                  "background: rgb(255, 56, 42);\n"
                                                  "}"))
            else:
                MsgWidget.setStyleSheet(_fromUtf8("QWidget{\n"
                                               "color : #ffffff;\n"
                                               "border-radius: 10px;\n"
                                               "background: rgb(110, 110, 255);\n"
                                               "}"))
        else:
            MsgWidget.setStyleSheet(_fromUtf8("QWidget{\n"
                                              "color : #ffffff;\n"
                                              "border-radius: 10px;\n"
                                              "background: rgb(85, 0, 255);\n"
                                              "}"))

        MsgWidget.setObjectName(_fromUtf8("MsgWidget"))


        horizontalLayout_11 = QtGui.QHBoxLayout(MsgWidget)
        horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        horizontalLayout_11.setContentsMargins(0, 4, -1, -1)
        horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        if nome:
            clienteNome = QtGui.QLabel(MsgWidget)
            clienteNome.setObjectName(_fromUtf8("clienteNome"))
            clienteNome.setText(nome)
            horizontalLayout_11.addWidget(clienteNome)

        mensagem = QtGui.QLabel(MsgWidget)
        mensagem.setObjectName(_fromUtf8("Mensagem"))
        mensagem.setText(msg)
        horizontalLayout_11.addWidget(mensagem)





        self.msglist.append(MsgWidget)
        return MsgWidget

    def enviar(self):

        self.verticalLayout.removeItem(self.spacerItem)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

        self.qtMsg += 1
        self.verticalLayout.addWidget(self.newMsg(self.qtMsg,self.textEdit.text()))

        self.verticalLayout.addItem(self.spacerItem)

        self.cliente.post(str(self.textEdit.text()+"\n").encode())
        self.textEdit.clear()
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def receber(self,nome,msg):
        self.verticalLayout.removeItem(self.spacerItem)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

        self.qtMsg += 1
        self.verticalLayout.addWidget(self.newMsg(self.qtMsg,msg,nome))
        self.verticalLayout.addItem(self.spacerItem)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def getData(self):
        self.cliente.getData()


    def updateStatus(self, nome,msg):
        self.receber(nome,msg)
