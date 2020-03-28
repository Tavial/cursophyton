# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_generador.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_numero1 = QtWidgets.QLabel(self.centralwidget)
        self.etq_numero1.setGeometry(QtCore.QRect(70, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_numero1.setFont(font)
        self.etq_numero1.setObjectName("etq_numero1")
        self.etq_numero2 = QtWidgets.QLabel(self.centralwidget)
        self.etq_numero2.setGeometry(QtCore.QRect(70, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_numero2.setFont(font)
        self.etq_numero2.setObjectName("etq_numero2")
        self.spinNumero1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinNumero1.setGeometry(QtCore.QRect(220, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinNumero1.setFont(font)
        self.spinNumero1.setObjectName("spinNumero1")
        self.spinNumero2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinNumero2.setGeometry(QtCore.QRect(220, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinNumero2.setFont(font)
        self.spinNumero2.setObjectName("spinNumero2")
        self.etq_generado = QtWidgets.QLabel(self.centralwidget)
        self.etq_generado.setGeometry(QtCore.QRect(70, 290, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_generado.setFont(font)
        self.etq_generado.setObjectName("etq_generado")
        self.textGenerado = QtWidgets.QTextBrowser(self.centralwidget)
        self.textGenerado.setGeometry(QtCore.QRect(220, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textGenerado.setFont(font)
        self.textGenerado.setObjectName("textGenerado")
        self.botonGenerar = QtWidgets.QPushButton(self.centralwidget)
        self.botonGenerar.setGeometry(QtCore.QRect(220, 380, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.botonGenerar.setFont(font)
        self.botonGenerar.setObjectName("botonGenerar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generador de números"))
        self.etq_numero1.setText(_translate("MainWindow", "Número 1"))
        self.etq_numero2.setText(_translate("MainWindow", "Número 2"))
        self.etq_generado.setText(_translate("MainWindow", "Número generado"))
        self.botonGenerar.setText(_translate("MainWindow", "Generar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
