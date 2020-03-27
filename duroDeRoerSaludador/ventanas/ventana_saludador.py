# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_saludador.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_saludo = QtWidgets.QLabel(self.centralwidget)
        self.etq_saludo.setGeometry(QtCore.QRect(160, 80, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.etq_saludo.setFont(font)
        self.etq_saludo.setObjectName("etq_saludo")
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(160, 140, 341, 31))
        self.nombre.setObjectName("nombre")
        self.boton_saludo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_saludo.setGeometry(QtCore.QRect(240, 210, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.boton_saludo.setFont(font)
        self.boton_saludo.setObjectName("boton_saludo")
        self.etq_resultado = QtWidgets.QLabel(self.centralwidget)
        self.etq_resultado.setGeometry(QtCore.QRect(160, 340, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.etq_resultado.setFont(font)
        self.etq_resultado.setText("")
        self.etq_resultado.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saludador"))
        self.etq_saludo.setText(_translate("MainWindow", "Escribe un nombre para saludar:"))
        self.boton_saludo.setText(_translate("MainWindow", "Saludar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
