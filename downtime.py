# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/HMI/downtimeform.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downtimeForm(object):
    def setupUi(self, downtimeForm):
        downtimeForm.setObjectName("downtimeForm")
        downtimeForm.resize(800, 480)
        self.label = QtWidgets.QLabel(downtimeForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/user/AppData/Local/Programs/Python/Python37-32/Scripts/HMI_v5/img_dt.png"))
        self.label.setObjectName("label")

        self.retranslateUi(downtimeForm)
        QtCore.QMetaObject.connectSlotsByName(downtimeForm)

    def retranslateUi(self, downtimeForm):
        _translate = QtCore.QCoreApplication.translate
        downtimeForm.setWindowTitle(_translate("downtimeForm", "Form"))

