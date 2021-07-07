# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuColores.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from MarcadorVirtual import *

rosaBajo = np.array([135, 100, 20], np.uint8)
rosaAlto = np.array([175, 255, 255], np.uint8)

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

amarilloBajo = np.array([15, 100, 20], np.uint8)
amarilloAlto = np.array([45, 255, 255], np.uint8)

rojoBajo = np.array([0, 100, 20], np.uint8)
rojoAlto = np.array([5, 255, 255], np.uint8)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 311)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.lapizRosa)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 160, 81, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.lapizAzul)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 160, 75, 21))
        self.pushButton_3.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.lapizAmarillo)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 160, 75, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.lapizRojo)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 60, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Lápiz Rosado"))
        self.pushButton_2.setText(_translate("Dialog", "Lápiz Azul"))
        self.pushButton_3.setText(_translate("Dialog", "Lápiz Amarillo"))
        self.pushButton_4.setText(_translate("Dialog", "Lápiz Rojo"))
        self.label.setText(_translate("Dialog", "Cambiar lápiz virtual"))

    def lapizRosa(self):
        Pizarra(rosaBajo, rosaAlto)
    def lapizAzul(self):
        Pizarra(azulBajo, azulAlto)
    def lapizAmarillo(self):
        Pizarra(amarilloBajo, amarilloAlto)
    def lapizRojo(self):
        Pizarra(rojoBajo, rojoAlto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

