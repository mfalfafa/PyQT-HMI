# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\Rpi3\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pb_off = QtWidgets.QPushButton(self.centralWidget)
        self.pb_off.setGeometry(QtCore.QRect(610, 390, 171, 61))
        self.pb_off.setObjectName("pb_off")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(510, 20, 271, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pb_on = QtWidgets.QPushButton(self.centralWidget)
        self.pb_on.setGeometry(QtCore.QRect(430, 390, 171, 61))
        self.pb_on.setObjectName("pb_on")
        self.lbl1 = QtWidgets.QLabel(self.centralWidget)
        self.lbl1.setGeometry(QtCore.QRect(490, 360, 71, 16))
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(self.centralWidget)
        self.lbl2.setGeometry(QtCore.QRect(650, 360, 61, 16))
        self.lbl2.setObjectName("lbl2")
        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setGeometry(QtCore.QRect(110, 231, 171, 41))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 290, 171, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lbl3 = QtWidgets.QLabel(self.centralWidget)
        self.lbl3.setGeometry(QtCore.QRect(300, 310, 151, 16))
        self.lbl3.setObjectName("lbl3")
        self.pb_insert = QtWidgets.QPushButton(self.centralWidget)
        self.pb_insert.setGeometry(QtCore.QRect(210, 350, 75, 23))
        self.pb_insert.setObjectName("pb_insert")
        self.lbl4 = QtWidgets.QLabel(self.centralWidget)
        self.lbl4.setGeometry(QtCore.QRect(290, 240, 151, 16))
        self.lbl4.setObjectName("lbl4")
        self.lbl5 = QtWidgets.QLabel(self.centralWidget)
        self.lbl5.setGeometry(QtCore.QRect(300, 290, 151, 16))
        self.lbl5.setObjectName("lbl5")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 256, 192))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.lbl6 = QtWidgets.QLabel(self.centralWidget)
        self.lbl6.setGeometry(QtCore.QRect(290, 150, 151, 16))
        self.lbl6.setObjectName("lbl6")
        self.pb_dialog = QtWidgets.QPushButton(self.centralWidget)
        self.pb_dialog.setGeometry(QtCore.QRect(460, 140, 111, 31))
        self.pb_dialog.setObjectName("pb_dialog")
        self.pb_exit = QtWidgets.QPushButton(self.centralWidget)
        self.pb_exit.setGeometry(QtCore.QRect(460, 190, 111, 31))
        self.pb_exit.setObjectName("pb_exit")
        self.lbl_data1 = QtWidgets.QLabel(self.centralWidget)
        self.lbl_data1.setGeometry(QtCore.QRect(610, 240, 46, 14))
        self.lbl_data1.setObjectName("lbl_data1")
        self.lbl_data2 = QtWidgets.QLabel(self.centralWidget)
        self.lbl_data2.setGeometry(QtCore.QRect(610, 270, 46, 14))
        self.lbl_data2.setObjectName("lbl_data2")
        self.lbl_data3 = QtWidgets.QLabel(self.centralWidget)
        self.lbl_data3.setGeometry(QtCore.QRect(610, 300, 46, 14))
        self.lbl_data3.setObjectName("lbl_data3")
        self.lbl7 = QtWidgets.QLabel(self.centralWidget)
        self.lbl7.setGeometry(QtCore.QRect(20, 440, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl7.setFont(font)
        self.lbl7.setObjectName("lbl7")
        self.lbl8 = QtWidgets.QLabel(self.centralWidget)
        self.lbl8.setGeometry(QtCore.QRect(150, 440, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl8.setFont(font)
        self.lbl8.setObjectName("lbl8")
        self.le1 = QtWidgets.QLineEdit(self.centralWidget)
        self.le1.setGeometry(QtCore.QRect(390, 290, 191, 31))
        self.le1.setObjectName("le1")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_off.setText(_translate("MainWindow", "OFF"))
        self.pb_on.setText(_translate("MainWindow", "ON"))
        self.lbl1.setText(_translate("MainWindow", "TextLabel"))
        self.lbl2.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Select 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Select 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Select 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Select 5"))
        self.lbl3.setText(_translate("MainWindow", "TextLabel"))
        self.pb_insert.setText(_translate("MainWindow", "Insert"))
        self.lbl4.setText(_translate("MainWindow", "TextLabel"))
        self.lbl5.setText(_translate("MainWindow", "TextLabel"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Item 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Item 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Item 4"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Item 5"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Item 6"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Item 7"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Item 8"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Item 9"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Item 10"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "Item 11"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "Item 12"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "Item 13"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lbl6.setText(_translate("MainWindow", "TextLabel"))
        self.pb_dialog.setText(_translate("MainWindow", "Dialog"))
        self.pb_exit.setText(_translate("MainWindow", "Exit"))
        self.lbl_data1.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_data2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_data3.setText(_translate("MainWindow", "TextLabel"))
        self.lbl7.setText(_translate("MainWindow", "Serial Data :"))
        self.lbl8.setText(_translate("MainWindow", "0"))

