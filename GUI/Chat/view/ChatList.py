# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatList.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatList(object):
    def setupUi(self, ChatList):
        ChatList.setObjectName("ChatList")
        ChatList.resize(361, 602)
        self.centralwidget = QtWidgets.QWidget(ChatList)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.personal_chat = QtWidgets.QPushButton(self.centralwidget)
        self.personal_chat.setObjectName("personal_chat")
        self.gridLayout.addWidget(self.personal_chat, 5, 0, 1, 2)
        self.create_group = QtWidgets.QPushButton(self.centralwidget)
        self.create_group.setObjectName("create_group")
        self.gridLayout.addWidget(self.create_group, 6, 0, 1, 2)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setObjectName("refresh")
        self.gridLayout.addWidget(self.refresh, 7, 0, 1, 2)
        self.chat_list = QtWidgets.QListWidget(self.centralwidget)
        self.chat_list.setObjectName("chat_list")
        self.gridLayout.addWidget(self.chat_list, 0, 0, 1, 2)
        self.UserID = QtWidgets.QLabel(self.centralwidget)
        self.UserID.setObjectName("UserID")
        self.gridLayout.addWidget(self.UserID, 2, 0, 1, 1)
        self.Value = QtWidgets.QLabel(self.centralwidget)
        self.Value.setObjectName("Value")
        self.gridLayout.addWidget(self.Value, 3, 0, 1, 1)
        ChatList.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChatList)
        self.statusbar.setObjectName("statusbar")
        ChatList.setStatusBar(self.statusbar)

        self.retranslateUi(ChatList)
        QtCore.QMetaObject.connectSlotsByName(ChatList)

    def retranslateUi(self, ChatList):
        _translate = QtCore.QCoreApplication.translate
        ChatList.setWindowTitle(_translate("ChatList", "MainWindow"))
        self.personal_chat.setText(_translate("ChatList", "Personal Chat"))
        self.create_group.setText(_translate("ChatList", "Create Group"))
        self.refresh.setText(_translate("ChatList", "Refresh"))
        self.UserID.setText(_translate("ChatList", "User ID:"))
        self.Value.setText(_translate("ChatList", "Value"))
