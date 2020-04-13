# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_copiar_pegar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaCopiarPegar(object):
    def setupUi(self, ventanaCopiarPegar):
        ventanaCopiarPegar.setObjectName("ventanaCopiarPegar")
        ventanaCopiarPegar.resize(400, 260)
        self.line_origen = QtWidgets.QLineEdit(ventanaCopiarPegar)
        self.line_origen.setGeometry(QtCore.QRect(30, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_origen.setFont(font)
        self.line_origen.setObjectName("line_origen")
        self.line_destino = QtWidgets.QLineEdit(ventanaCopiarPegar)
        self.line_destino.setGeometry(QtCore.QRect(30, 190, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_destino.setFont(font)
        self.line_destino.setObjectName("line_destino")
        self.boton_copiar = QtWidgets.QPushButton(ventanaCopiarPegar)
        self.boton_copiar.setGeometry(QtCore.QRect(140, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_copiar.setFont(font)
        self.boton_copiar.setObjectName("boton_copiar")
        self.boton_pegar = QtWidgets.QPushButton(ventanaCopiarPegar)
        self.boton_pegar.setGeometry(QtCore.QRect(140, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_pegar.setFont(font)
        self.boton_pegar.setObjectName("boton_pegar")

        self.retranslateUi(ventanaCopiarPegar)
        self.boton_copiar.pressed.connect(self.line_origen.selectAll)
        self.boton_copiar.released.connect(self.line_origen.copy)
        self.boton_pegar.pressed.connect(self.line_destino.paste)
        QtCore.QMetaObject.connectSlotsByName(ventanaCopiarPegar)

    def retranslateUi(self, ventanaCopiarPegar):
        _translate = QtCore.QCoreApplication.translate
        ventanaCopiarPegar.setWindowTitle(_translate("ventanaCopiarPegar", "Copiar y Pegar"))
        self.boton_copiar.setText(_translate("ventanaCopiarPegar", "Copiar"))
        self.boton_pegar.setText(_translate("ventanaCopiarPegar", "Pegar"))
