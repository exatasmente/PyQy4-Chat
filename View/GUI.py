# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientGui.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 200)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(193, 163))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.LoginWidget = QtGui.QWidget(self.centralwidget)
        self.LoginWidget.setEnabled(True)
        self.LoginWidget.setGeometry(QtCore.QRect(60, 30, 191, 162))
        self.LoginWidget.setMinimumSize(QtCore.QSize(191, 161))
        self.LoginWidget.setMaximumSize(QtCore.QSize(192, 162))
        self.LoginWidget.setObjectName(_fromUtf8("LoginWidget"))
        self.loginField = QtGui.QLineEdit(self.LoginWidget)
        self.loginField.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.loginField.setObjectName(_fromUtf8("loginField"))
        self.NomeLabel = QtGui.QLabel(self.LoginWidget)
        self.NomeLabel.setGeometry(QtCore.QRect(40, 40, 121, 20))
        self.NomeLabel.setObjectName(_fromUtf8("NomeLabel"))
        self.EntrarBtn = QtGui.QPushButton(self.LoginWidget)
        self.EntrarBtn.setGeometry(QtCore.QRect(60, 100, 83, 24))
        self.EntrarBtn.setObjectName(_fromUtf8("EntrarBtn"))
        self.loginField.raise_()
        self.NomeLabel.raise_()
        self.EntrarBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.NomeLabel.setText(_translate("MainWindow", "Nome De Usuário", None))
        self.EntrarBtn.setText(_translate("MainWindow", "Entrar", None))
