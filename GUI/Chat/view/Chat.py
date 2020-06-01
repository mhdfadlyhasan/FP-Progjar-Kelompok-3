# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupChatUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chat_window(object):
    def setupUi(self, chat_window):
        chat_window.setObjectName("chat_window")
        chat_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(chat_window)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 798, 571))
        self.centralwidget.setObjectName("centralwidget")
        self.show_member = QtWidgets.QPushButton(self.centralwidget)
        self.show_member.setGeometry(QtCore.QRect(690, 10, 75, 23))
        self.show_member.setObjectName("show_member")
        self.group_name = QtWidgets.QLabel(self.centralwidget)
        self.group_name.setGeometry(QtCore.QRect(30, 0, 91, 51))
        self.group_name.setObjectName("group_name")
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
        self.invite = QtWidgets.QPushButton(self.centralwidget)
        self.invite.setGeometry(QtCore.QRect(610, 10, 75, 23))
        self.invite.setObjectName("invite")
        self.message_list = QtWidgets.QTextEdit(self.centralwidget)
        self.message_list.setGeometry(QtCore.QRect(10, 70, 781, 421))
        self.message_list.setObjectName("message_list")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 540, 781, 31))
        self.input.setObjectName("input")
        self.statusbar = QtWidgets.QStatusBar(chat_window)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(chat_window)
        QtCore.QMetaObject.connectSlotsByName(chat_window)

    def retranslateUi(self, chat_window):
        _translate = QtCore.QCoreApplication.translate
        chat_window.setWindowTitle(_translate("chat_window", "MainWindow"))
        self.show_member.setText(_translate("chat_window", "Members"))
        self.group_name.setText(_translate("chat_window", "Group Name"))
        self.file.setText(_translate("chat_window", "File"))
        self.invite.setText(_translate("chat_window", "Invite"))
