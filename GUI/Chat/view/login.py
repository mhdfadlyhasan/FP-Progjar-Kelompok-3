# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(449, 350)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(160, 0, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(80, 120, 301, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 190, 301, 31))
        self.password.setObjectName("password")
        self.username_text = QtWidgets.QLabel(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(200, 100, 61, 16))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLabel(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(200, 170, 61, 16))
        self.password_text.setObjectName("password_text")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.login.setObjectName("login")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuFTP = QtWidgets.QMenu(self.menubar)
        self.menuFTP.setObjectName("menuFTP")
        Login.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(Login)
        self.actionExit.setObjectName("actionExit")
        self.actionLaunchFTP = QtWidgets.QAction(Login)
        self.actionLaunchFTP.setObjectName("actionLaunchFTP")
        self.menuMenu.addAction(self.actionExit)
        self.menuFTP.addAction(self.actionLaunchFTP)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuFTP.menuAction())

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Title.setText(_translate("Login", "JarChat"))
        self.username_text.setText(_translate("Login", "Username"))
        self.password_text.setText(_translate("Login", "Password "))
        self.login.setText(_translate("Login", "Login"))
        self.menuMenu.setTitle(_translate("Login", "Menu"))
        self.menuFTP.setTitle(_translate("Login", "FTP"))
        self.actionExit.setText(_translate("Login", "Exit"))
        self.actionExit.setShortcut(_translate("Login", "Ctrl+Q"))
        self.actionLaunchFTP.setText(_translate("Login", "Launch FTP"))
        self.actionLaunchFTP.setStatusTip(_translate("Login", "Launch FTP Client"))
