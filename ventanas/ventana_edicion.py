# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_edicion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaEdicion(object):
    def setupUi(self, ventanaEdicion):
        ventanaEdicion.setObjectName("ventanaEdicion")
        ventanaEdicion.resize(534, 499)
        self.centralwidget = QtWidgets.QWidget(ventanaEdicion)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_tema = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tema.setGeometry(QtCore.QRect(40, 270, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_tema.setFont(font)
        self.lbl_tema.setObjectName("lbl_tema")
        self.boton_modificar_revista = QtWidgets.QPushButton(self.centralwidget)
        self.boton_modificar_revista.setGeometry(QtCore.QRect(110, 380, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_modificar_revista.setFont(font)
        self.boton_modificar_revista.setObjectName("boton_modificar_revista")
        self.lbl_principal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_principal.setGeometry(QtCore.QRect(110, 40, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_principal.setFont(font)
        self.lbl_principal.setObjectName("lbl_principal")
        self.entrada_tema = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_tema.setGeometry(QtCore.QRect(110, 270, 301, 31))
        self.entrada_tema.setObjectName("entrada_tema")
        self.entrada_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_titulo.setGeometry(QtCore.QRect(110, 130, 371, 31))
        self.entrada_titulo.setObjectName("entrada_titulo")
        self.lbl_precio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_precio.setGeometry(QtCore.QRect(40, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setObjectName("lbl_precio")
        self.entrada_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_precio.setGeometry(QtCore.QRect(110, 200, 151, 31))
        self.entrada_precio.setObjectName("entrada_precio")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(40, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")
        ventanaEdicion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventanaEdicion)
        self.statusbar.setObjectName("statusbar")
        ventanaEdicion.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaEdicion)
        QtCore.QMetaObject.connectSlotsByName(ventanaEdicion)

    def retranslateUi(self, ventanaEdicion):
        _translate = QtCore.QCoreApplication.translate
        ventanaEdicion.setWindowTitle(_translate("ventanaEdicion", "Editar revista"))
        self.lbl_tema.setText(_translate("ventanaEdicion", "Tema:"))
        self.boton_modificar_revista.setText(_translate("ventanaEdicion", "MODIFICAR REVISTA"))
        self.lbl_principal.setText(_translate("ventanaEdicion", "Modifica los datos de la revista: "))
        self.lbl_precio.setText(_translate("ventanaEdicion", "Precio:"))
        self.lbl_titulo.setText(_translate("ventanaEdicion", "Título: "))
