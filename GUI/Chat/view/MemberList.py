# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemberList.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_member(object):
    def setupUi(self, member):
        member.setObjectName("member")
        member.resize(274, 475)
        self.centralwidget = QtWidgets.QWidget(member)
        self.centralwidget.setObjectName("centralwidget")
        self.member_list = QtWidgets.QListWidget(self.centralwidget)
        self.member_list.setGeometry(QtCore.QRect(10, 10, 256, 441))
        self.member_list.setObjectName("member_list")
        member.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(member)
        self.statusbar.setObjectName("statusbar")
        member.setStatusBar(self.statusbar)

        self.retranslateUi(member)
        QtCore.QMetaObject.connectSlotsByName(member)

    def retranslateUi(self, member):
        _translate = QtCore.QCoreApplication.translate
        member.setWindowTitle(_translate("member", "Member List"))
