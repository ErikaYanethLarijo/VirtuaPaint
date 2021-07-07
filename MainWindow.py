import sys
import cv2
import PyQt5
from PyQt5 import uic, QtWidgets
from MarcadorVirtual import *
from Filtros import *
from Menu_ui import *
from MenuColores_ui import Ui_Dialog
from Guardar import guardar
from MenuCuentos_ui import Ui_MainWindow
import os

qtCreatorFile = "Menu.ui"
Ui_VirtualPaint, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_VirtualPaint):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_VirtualPaint.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.abrir)
        self.pushButton_2.clicked.connect(self.abrir2)

    def abrir(self):
        self.ventana2=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.ventana2)
        self.ventana2.show()
    def abrir2(self):
        self.ventana3=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.ventana3)
        self.ventana3.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
