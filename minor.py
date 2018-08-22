# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/HMI/minorform.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_minorForm(object):
    def setupUi(self, minorForm):
        minorForm.setObjectName("minorForm")
        minorForm.resize(800, 480)
        self.label = QtWidgets.QLabel(minorForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/pi/PyQt-HMI/img_minor.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.retranslateUi(minorForm)
        QtCore.QMetaObject.connectSlotsByName(minorForm)

    def retranslateUi(self, minorForm):
        _translate = QtCore.QCoreApplication.translate
        minorForm.setWindowTitle(_translate("minorForm", "Form"))

