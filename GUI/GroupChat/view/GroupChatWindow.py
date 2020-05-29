# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupChatUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from model.GroupChatClientModel import GroupChatClientModel

class Ui_group_chat_window(object):

    model = GroupChatClientModel()
    username = None

    # GUI group chat window
    def setupUi(self, group_chat_window):
        group_chat_window.setObjectName("group_chat_window")
        group_chat_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(group_chat_window)
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
        self.statusbar = QtWidgets.QStatusBar(group_chat_window)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(group_chat_window)
        QtCore.QMetaObject.connectSlotsByName(group_chat_window)

        # Client Connect
        self.username = self.model.connect()

    def retranslateUi(self, group_chat_window):
        _translate = QtCore.QCoreApplication.translate
        group_chat_window.setWindowTitle(_translate("group_chat_window", "Chat Window"))
        self.show_member.setText(_translate("group_chat_window", "Members"))
        self.group_name.setText(_translate("group_chat_window", "Group Name"))
        self.file.setText(_translate("group_chat_window", "File"))
        self.invite.setText(_translate("group_chat_window", "Invite"))

    # Custom Functions
    def message_input(self):

        # Ambil input dari GUI
        message = self.input.text()
        self.input.clear()

        # Print input user di message list
        if (message[0] == '<'):
            pass
        else:
            self.message_list.append(str(self.username) + ': ' + str(message))
        
        # Send message ke server setelah diproses di client model
        self.model.group_chat(message)

