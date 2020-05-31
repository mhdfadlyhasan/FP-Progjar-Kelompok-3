# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatlist.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_list = QtWidgets.QListWidget(self.centralwidget)
        self.chat_list.setObjectName("chat_list")
        item = QtWidgets.QListWidgetItem()
        self.chat_list.addItem(item)
        self.verticalLayout.addWidget(self.chat_list)
        self.personal_chat = QtWidgets.QPushButton(self.centralwidget)
        self.personal_chat.setObjectName("personal_chat")
        self.verticalLayout.addWidget(self.personal_chat)
        self.create_group = QtWidgets.QPushButton(self.centralwidget)
        self.create_group.setObjectName("create_group")
        self.verticalLayout.addWidget(self.create_group)
        self.join_group = QtWidgets.QPushButton(self.centralwidget)
        self.join_group.setObjectName("join_group")
        self.verticalLayout.addWidget(self.join_group)
        ChatList.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChatList)
        self.statusbar.setObjectName("statusbar")
        ChatList.setStatusBar(self.statusbar)

        self.retranslateUi(ChatList)
        QtCore.QMetaObject.connectSlotsByName(ChatList)

    def retranslateUi(self, ChatList):
        _translate = QtCore.QCoreApplication.translate
        ChatList.setWindowTitle(_translate("ChatList", "Chat List"))
        __sortingEnabled = self.chat_list.isSortingEnabled()
        self.chat_list.setSortingEnabled(False)
        item = self.chat_list.item(0)
        item.setText(_translate("ChatList", "List_Item"))
        self.chat_list.setSortingEnabled(__sortingEnabled)
        self.personal_chat.setText(_translate("ChatList", "Personal Chat"))
        self.create_group.setText(_translate("ChatList", "Create Group"))
        self.join_group.setText(_translate("ChatList", "Join Group"))
