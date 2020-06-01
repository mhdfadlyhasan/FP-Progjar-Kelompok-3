# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonalChatUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_personal_chat_window(object):
    def setupUi(self, personal_chat_window):
        personal_chat_window.setObjectName("personal_chat_window")
        personal_chat_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(personal_chat_window)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 798, 571))
        self.centralwidget.setObjectName("centralwidget")
        self.personal_name = QtWidgets.QLabel(self.centralwidget)
        self.personal_name.setGeometry(QtCore.QRect(30, 0, 91, 51))
        self.personal_name.setObjectName("personal_name")
        self.upper_line = QtWidgets.QFrame(self.centralwidget)
        self.upper_line.setGeometry(QtCore.QRect(0, 50, 801, 16))
        self.upper_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.upper_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.upper_line.setObjectName("upper_line")
        self.bottomline = QtWidgets.QFrame(self.centralwidget)
        self.bottomline.setGeometry(QtCore.QRect(-3, 490, 801, 20))
        self.bottomline.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottomline.setObjectName("bottomline")
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(10, 510, 75, 23))
        self.file.setObjectName("file")
        self.message_list = QtWidgets.QTextEdit(self.centralwidget)
        self.message_list.setGeometry(QtCore.QRect(10, 70, 781, 421))
        self.message_list.setObjectName("message_list")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 540, 781, 31))
        self.input.setObjectName("input")
        self.statusbar = QtWidgets.QStatusBar(personal_chat_window)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(personal_chat_window)
        QtCore.QMetaObject.connectSlotsByName(personal_chat_window)

    def retranslateUi(self, personal_chat_window):
        _translate = QtCore.QCoreApplication.translate
        personal_chat_window.setWindowTitle(_translate("personal_chat_window", "MainWindow"))
        self.personal_name.setText(_translate("personal_chat_window", "Personal Chat"))
        self.file.setText(_translate("personal_chat_window", "File"))
