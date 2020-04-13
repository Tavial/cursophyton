# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaCalculadora(object):
    def setupUi(self, ventanaCalculadora):
        ventanaCalculadora.setObjectName("ventanaCalculadora")
        ventanaCalculadora.resize(528, 357)
        self.etq_primer_numero = QtWidgets.QLabel(ventanaCalculadora)
        self.etq_primer_numero.setGeometry(QtCore.QRect(20, 50, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_primer_numero.setFont(font)
        self.etq_primer_numero.setObjectName("etq_primer_numero")
        self.etq_segundo_numero = QtWidgets.QLabel(ventanaCalculadora)
        self.etq_segundo_numero.setGeometry(QtCore.QRect(20, 110, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_segundo_numero.setFont(font)
        self.etq_segundo_numero.setObjectName("etq_segundo_numero")
        self.line_primer_numero = QtWidgets.QLineEdit(ventanaCalculadora)
        self.line_primer_numero.setGeometry(QtCore.QRect(270, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_primer_numero.setFont(font)
        self.line_primer_numero.setObjectName("line_primer_numero")
        self.line_segundo_numero = QtWidgets.QLineEdit(ventanaCalculadora)
        self.line_segundo_numero.setGeometry(QtCore.QRect(270, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_segundo_numero.setFont(font)
        self.line_segundo_numero.setObjectName("line_segundo_numero")
        self.boton_suma = QtWidgets.QPushButton(ventanaCalculadora)
        self.boton_suma.setGeometry(QtCore.QRect(20, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boton_suma.setFont(font)
        self.boton_suma.setObjectName("boton_suma")
        self.boton_resta = QtWidgets.QPushButton(ventanaCalculadora)
        self.boton_resta.setGeometry(QtCore.QRect(150, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boton_resta.setFont(font)
        self.boton_resta.setObjectName("boton_resta")
        self.boton_producto = QtWidgets.QPushButton(ventanaCalculadora)
        self.boton_producto.setGeometry(QtCore.QRect(280, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boton_producto.setFont(font)
        self.boton_producto.setObjectName("boton_producto")
        self.boton_cociente = QtWidgets.QPushButton(ventanaCalculadora)
        self.boton_cociente.setGeometry(QtCore.QRect(420, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.boton_cociente.setFont(font)
        self.boton_cociente.setObjectName("boton_cociente")
        self.line_resultado = QtWidgets.QLineEdit(ventanaCalculadora)
        self.line_resultado.setGeometry(QtCore.QRect(270, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_resultado.setFont(font)
        self.line_resultado.setObjectName("line_resultado")
        self.etq_resultado = QtWidgets.QLabel(ventanaCalculadora)
        self.etq_resultado.setGeometry(QtCore.QRect(30, 290, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_resultado.setFont(font)
        self.etq_resultado.setObjectName("etq_resultado")

        self.retranslateUi(ventanaCalculadora)
        QtCore.QMetaObject.connectSlotsByName(ventanaCalculadora)

    def retranslateUi(self, ventanaCalculadora):
        _translate = QtCore.QCoreApplication.translate
        ventanaCalculadora.setWindowTitle(_translate("ventanaCalculadora", "Calculadora"))
        self.etq_primer_numero.setText(_translate("ventanaCalculadora", "Introduce el primer número:"))
        self.etq_segundo_numero.setText(_translate("ventanaCalculadora", "Introduce el segundo número:"))
        self.boton_suma.setText(_translate("ventanaCalculadora", "+"))
        self.boton_resta.setText(_translate("ventanaCalculadora", "-"))
        self.boton_producto.setText(_translate("ventanaCalculadora", "X"))
        self.boton_cociente.setText(_translate("ventanaCalculadora", "/"))
        self.etq_resultado.setText(_translate("ventanaCalculadora", "Resultado:"))
