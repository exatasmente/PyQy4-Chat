# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListaCanais.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


class Ui_ListaCanais(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(216, 458)
        MainWindow.setMinimumSize(QtCore.QSize(216, 458))
        MainWindow.setMaximumSize(QtCore.QSize(216, 458))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nomeCliente = QtGui.QLabel(self.centralwidget)
        self.nomeCliente.setObjectName(_fromUtf8("nomeCliente"))
        self.verticalLayout_2.addWidget(self.nomeCliente)
        self.criarCanalBtn = QtGui.QPushButton(self.centralwidget)
        self.criarCanalBtn.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.criarCanalBtn)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(198, 300))
        self.scrollArea.setMaximumSize(QtCore.QSize(198, 400))
        self.scrollArea.setFrameShape(QtGui.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaContainer = QtGui.QWidget()
        self.scrollAreaContainer.setGeometry(QtCore.QRect(0, 0, 187, 347))
        self.scrollAreaContainer.setObjectName(_fromUtf8("scrollAreaContainer"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaContainer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea.setWidget(self.scrollAreaContainer)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Lista de Canais", "Lista de Canais", None))
        self.nomeCliente.setText(_translate("MainWindow", "Nome Cliente", None))
        self.criarCanalBtn.setText(_translate("MainWindow", "Criar Canal", None))
