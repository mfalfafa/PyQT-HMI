# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\my-dilalog\my_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_my_dialog(object):
    def setupUi(self, my_dialog):
        my_dialog.setObjectName("my_dialog")
        my_dialog.resize(800, 480)
        self.pb_exit = QtWidgets.QPushButton(my_dialog)
        self.pb_exit.setGeometry(QtCore.QRect(690, 420, 91, 41))
        self.pb_exit.setObjectName("pb_exit")
        self.label = QtWidgets.QLabel(my_dialog)
        self.label.setGeometry(QtCore.QRect(100, 60, 46, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(my_dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 46, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(my_dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 46, 14))
        self.label_3.setObjectName("label_3")
        self.le1 = QtWidgets.QLineEdit(my_dialog)
        self.le1.setGeometry(QtCore.QRect(160, 60, 161, 31))
        self.le1.setText("")
        self.le1.setObjectName("le1")
        self.le2 = QtWidgets.QLineEdit(my_dialog)
        self.le2.setGeometry(QtCore.QRect(160, 110, 161, 31))
        self.le2.setText("")
        self.le2.setObjectName("le2")
        self.le3 = QtWidgets.QLineEdit(my_dialog)
        self.le3.setGeometry(QtCore.QRect(160, 160, 161, 31))
        self.le3.setText("")
        self.le3.setObjectName("le3")
        self.pb_submit = QtWidgets.QPushButton(my_dialog)
        self.pb_submit.setGeometry(QtCore.QRect(240, 210, 81, 41))
        self.pb_submit.setObjectName("pb_submit")

        self.retranslateUi(my_dialog)
        QtCore.QMetaObject.connectSlotsByName(my_dialog)

    def retranslateUi(self, my_dialog):
        _translate = QtCore.QCoreApplication.translate
        my_dialog.setWindowTitle(_translate("my_dialog", "Form"))
        self.pb_exit.setText(_translate("my_dialog", "Back"))
        self.label.setText(_translate("my_dialog", "Param 1"))
        self.label_2.setText(_translate("my_dialog", "Param 2"))
        self.label_3.setText(_translate("my_dialog", "Param 3"))
        self.pb_submit.setText(_translate("my_dialog", "Submit"))

