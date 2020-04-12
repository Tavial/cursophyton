# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listados_lista.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaListadosLista(object):
    def setupUi(self, ventanaListadosLista):
        ventanaListadosLista.setObjectName("ventanaListadosLista")
        ventanaListadosLista.resize(1038, 883)
        self.centralwidget = QtWidgets.QWidget(ventanaListadosLista)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_principal = QtWidgets.QLabel(self.centralwidget)
        self.etq_principal.setGeometry(QtCore.QRect(380, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etq_principal.setFont(font)
        self.etq_principal.setFrameShape(QtWidgets.QFrame.Panel)
        self.etq_principal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.etq_principal.setObjectName("etq_principal")
        self.separador1 = QtWidgets.QFrame(self.centralwidget)
        self.separador1.setGeometry(QtCore.QRect(0, 40, 381, 20))
        self.separador1.setFrameShape(QtWidgets.QFrame.HLine)
        self.separador1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separador1.setObjectName("separador1")
        self.separador2 = QtWidgets.QFrame(self.centralwidget)
        self.separador2.setGeometry(QtCore.QRect(660, 40, 371, 20))
        self.separador2.setFrameShape(QtWidgets.QFrame.HLine)
        self.separador2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separador2.setObjectName("separador2")
        self.visor_listado = QtWidgets.QListWidget(self.centralwidget)
        self.visor_listado.setGeometry(QtCore.QRect(20, 90, 1001, 721))
        self.visor_listado.setObjectName("visor_listado")
        ventanaListadosLista.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventanaListadosLista)
        self.statusbar.setObjectName("statusbar")
        ventanaListadosLista.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaListadosLista)
        QtCore.QMetaObject.connectSlotsByName(ventanaListadosLista)

    def retranslateUi(self, ventanaListadosLista):
        _translate = QtCore.QCoreApplication.translate
        ventanaListadosLista.setWindowTitle(_translate("ventanaListadosLista", "Listado de productos"))
        self.etq_principal.setText(_translate("ventanaListadosLista", "    LISTA DE PRODUCTOS"))
