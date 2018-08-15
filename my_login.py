# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\Rpi3\my_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_my_login(object):
    def setupUi(self, my_login):
        my_login.setObjectName("my_login")
        my_login.resize(800, 480)
        self.lbl_login = QtWidgets.QLabel(my_login)
        self.lbl_login.setGeometry(QtCore.QRect(400, 250, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.lbl_info = QtWidgets.QLabel(my_login)
        self.lbl_info.setGeometry(QtCore.QRect(260, 340, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_info.setFont(font)
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_info.setText("")
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setObjectName("lbl_info")
        self.le_login = QtWidgets.QLineEdit(my_login)
        self.le_login.setGeometry(QtCore.QRect(260, 280, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_login.setFont(font)
        self.le_login.setPlaceholderText("")
        self.le_login.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.le_login.setObjectName("le_login")
        self.label = QtWidgets.QLabel(my_login)
        self.label.setGeometry(QtCore.QRect(340, 70, 171, 141))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("MMM.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(my_login)
        QtCore.QMetaObject.connectSlotsByName(my_login)

    def retranslateUi(self, my_login):
        _translate = QtCore.QCoreApplication.translate
        my_login.setWindowTitle(_translate("my_login", "Form"))
        self.lbl_login.setText(_translate("my_login", "LOGIN"))

