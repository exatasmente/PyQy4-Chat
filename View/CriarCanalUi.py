# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CriarCanalUi.ui'
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

class Ui_CriarCanal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 150)
        MainWindow.setMinimumSize(QtCore.QSize(400, 150))
        MainWindow.setMaximumSize(QtCore.QSize(400, 150))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Criar = QtGui.QPushButton(self.centralwidget)
        self.Criar.setGeometry(QtCore.QRect(170, 70, 83, 24))
        self.Criar.setObjectName(_fromUtf8("Criar"))
        self.NomeCanalInput = QtGui.QLineEdit(self.centralwidget)
        self.NomeCanalInput.setGeometry(QtCore.QRect(120, 27, 191, 31))
        self.NomeCanalInput.setObjectName(_fromUtf8("NomeCanalInput"))
        self.NomeCanal = QtGui.QLabel(self.centralwidget)
        self.NomeCanal.setGeometry(QtCore.QRect(6, 30, 111, 31))
        self.NomeCanal.setObjectName(_fromUtf8("NomeCanal"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Criar.setText(_translate("MainWindow", "Criar", None))
        self.NomeCanal.setText(_translate("MainWindow", "Nome do Canal", None))
