# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro_revista.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_principal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_principal.setGeometry(QtCore.QRect(100, 50, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_principal.setFont(font)
        self.lbl_principal.setObjectName("lbl_principal")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(30, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.entrada_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_titulo.setGeometry(QtCore.QRect(100, 140, 371, 31))
        self.entrada_titulo.setObjectName("entrada_titulo")
        self.entrada_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_precio.setGeometry(QtCore.QRect(100, 210, 151, 31))
        self.entrada_precio.setObjectName("entrada_precio")
        self.lbl_precio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_precio.setGeometry(QtCore.QRect(30, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setObjectName("lbl_precio")
        self.entrada_tema = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_tema.setGeometry(QtCore.QRect(100, 280, 301, 31))
        self.entrada_tema.setObjectName("entrada_tema")
        self.lbl_tema = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tema.setGeometry(QtCore.QRect(30, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_tema.setFont(font)
        self.lbl_tema.setObjectName("lbl_tema")
        self.boton_registrar_revista = QtWidgets.QPushButton(self.centralwidget)
        self.boton_registrar_revista.setGeometry(QtCore.QRect(100, 390, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_registrar_revista.setFont(font)
        self.boton_registrar_revista.setObjectName("boton_registrar_revista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registrar revista"))
        self.lbl_principal.setText(_translate("MainWindow", "Introduce los datos de la nueva revista: "))
        self.lbl_titulo.setText(_translate("MainWindow", "Título: "))
        self.lbl_precio.setText(_translate("MainWindow", "Precio:"))
        self.lbl_tema.setText(_translate("MainWindow", "Tema:"))
        self.boton_registrar_revista.setText(_translate("MainWindow", "REGISTRAR REVISTA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
