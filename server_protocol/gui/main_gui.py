# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 288)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 261, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.target = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.target.setObjectName("target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.user = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.user.setObjectName("user")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cores = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cores.setObjectName("cores")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cores)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.protocol = QtWidgets.QComboBox(self.formLayoutWidget)
        self.protocol.setObjectName("protocol")
        self.protocol.addItem("")
        self.protocol.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.protocol)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.open_dictionnary = QtWidgets.QPushButton(self.formLayoutWidget)
        self.open_dictionnary.setObjectName("open_dictionnary")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.open_dictionnary)
        self.password_file = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_file.setObjectName("password_file")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password_file)
        self.port = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.port.setObjectName("port")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.port)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.network_check = QtWidgets.QComboBox(self.formLayoutWidget)
        self.network_check.setObjectName("network_check")
        self.network_check.addItem("")
        self.network_check.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.network_check)
        self.quit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.quit.setObjectName("quit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.quit)
        self.RunAttack = QtWidgets.QPushButton(self.formLayoutWidget)
        self.RunAttack.setObjectName("RunAttack")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.RunAttack)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.target.setText(_translate("Dialog", "127.0.0.1"))
        self.label_10.setText(_translate("Dialog", "Target"))
        self.label_11.setText(_translate("Dialog", "Username"))
        self.user.setText(_translate("Dialog", "root"))
        self.label_6.setText(_translate("Dialog", "Cores"))
        self.cores.setText(_translate("Dialog", "4"))
        self.label_12.setText(_translate("Dialog", "Protocol"))
        self.protocol.setItemText(0, _translate("Dialog", "ssh"))
        self.protocol.setItemText(1, _translate("Dialog", "mysql"))
        self.label_13.setText(_translate("Dialog", "Port"))
        self.open_dictionnary.setText(_translate("Dialog", "Open Dictionnary"))
        self.port.setText(_translate("Dialog", "22"))
        self.label_14.setText(_translate("Dialog", "Network checks"))
        self.network_check.setItemText(0, _translate("Dialog", "yes"))
        self.network_check.setItemText(1, _translate("Dialog", "no"))
        self.quit.setText(_translate("Dialog", "Quit"))
        self.RunAttack.setText(_translate("Dialog", "Run Attack"))

