# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/HMI/login_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.resize(800, 480)
        self.le_login = QtWidgets.QLineEdit(login_form)
        self.le_login.setGeometry(QtCore.QRect(225, 250, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_login.setFont(font)
        self.le_login.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.le_login.setObjectName("le_login")
        self.label_5 = QtWidgets.QLabel(login_form)
        self.label_5.setGeometry(QtCore.QRect(686, 389, 114, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("corner.png"))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(login_form)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(login_form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 70, 60))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("MMM.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(login_form)
        self.label.setGeometry(QtCore.QRect(225, 200, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lbl_info = QtWidgets.QLabel(login_form)
        self.lbl_info.setGeometry(QtCore.QRect(225, 310, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info.setFont(font)
        self.lbl_info.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_info.setText("")
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setObjectName("lbl_info")
        self.label_14 = QtWidgets.QLabel(login_form)
        self.label_14.setGeometry(QtCore.QRect(549, 20, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.le_login.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.lbl_info.raise_()
        self.label_14.raise_()

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Form"))
        self.label_3.setText(_translate("login_form", "@MachineVision2018"))
        self.label.setText(_translate("login_form", "Tempelkan RFID"))
        self.label_14.setText(_translate("login_form", "HMI Packaging Line 23"))

