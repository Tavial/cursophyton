# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_borrado.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaDialogo(object):
    def setupUi(self, ventanaDialogo):
        ventanaDialogo.setObjectName("ventanaDialogo")
        ventanaDialogo.resize(341, 207)
        self.line_texto = QtWidgets.QLineEdit(ventanaDialogo)
        self.line_texto.setGeometry(QtCore.QRect(40, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_texto.setFont(font)
        self.line_texto.setText("")
        self.line_texto.setObjectName("line_texto")
        self.boton_borrar = QtWidgets.QPushButton(ventanaDialogo)
        self.boton_borrar.setGeometry(QtCore.QRect(40, 120, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_borrar.setFont(font)
        self.boton_borrar.setObjectName("boton_borrar")

        self.retranslateUi(ventanaDialogo)
        self.boton_borrar.clicked.connect(self.line_texto.clear)
        QtCore.QMetaObject.connectSlotsByName(ventanaDialogo)

    def retranslateUi(self, ventanaDialogo):
        _translate = QtCore.QCoreApplication.translate
        ventanaDialogo.setWindowTitle(_translate("ventanaDialogo", "Borrado"))
        self.boton_borrar.setText(_translate("ventanaDialogo", "Borrar"))
