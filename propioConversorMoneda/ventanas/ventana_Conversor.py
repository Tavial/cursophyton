# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_conversor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EtqIntroducir = QtWidgets.QLabel(self.centralwidget)
        self.EtqIntroducir.setGeometry(QtCore.QRect(50, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EtqIntroducir.setFont(font)
        self.EtqIntroducir.setObjectName("EtqIntroducir")
        self.etqTitulo = QtWidgets.QLabel(self.centralwidget)
        self.etqTitulo.setGeometry(QtCore.QRect(190, 10, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.etqTitulo.setFont(font)
        self.etqTitulo.setObjectName("etqTitulo")
        self.EtqDivisa = QtWidgets.QLabel(self.centralwidget)
        self.EtqDivisa.setGeometry(QtCore.QRect(390, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EtqDivisa.setFont(font)
        self.EtqDivisa.setObjectName("EtqDivisa")
        self.EditCantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.EditCantidad.setGeometry(QtCore.QRect(50, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditCantidad.setFont(font)
        self.EditCantidad.setObjectName("EditCantidad")
        self.EtqResultado = QtWidgets.QLabel(self.centralwidget)
        self.EtqResultado.setGeometry(QtCore.QRect(50, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EtqResultado.setFont(font)
        self.EtqResultado.setObjectName("EtqResultado")
        self.EditResultado = QtWidgets.QLineEdit(self.centralwidget)
        self.EditResultado.setGeometry(QtCore.QRect(50, 270, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditResultado.setFont(font)
        self.EditResultado.setObjectName("EditResultado")
        self.comboDivisa = QtWidgets.QComboBox(self.centralwidget)
        self.comboDivisa.setGeometry(QtCore.QRect(390, 130, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboDivisa.setFont(font)
        self.comboDivisa.setObjectName("comboDivisa")
        self.botonCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.botonCalcular.setGeometry(QtCore.QRect(390, 260, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.botonCalcular.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ventanas/iconoDiario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonCalcular.setIcon(icon)
        self.botonCalcular.setIconSize(QtCore.QSize(32, 32))
        self.botonCalcular.setObjectName("botonCalcular")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EtqIntroducir.setText(_translate("MainWindow", "Cantidad"))
        self.etqTitulo.setText(_translate("MainWindow", "CONVERSOR DE EUROS A OTRA DIVISA"))
        self.EtqDivisa.setText(_translate("MainWindow", "Pasar a: "))
        self.EtqResultado.setText(_translate("MainWindow", "Resultado"))
        self.botonCalcular.setText(_translate("MainWindow", "     Calcular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
