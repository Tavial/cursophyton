# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listados.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaListados(object):
    def setupUi(self, ventanaListados):
        ventanaListados.setObjectName("ventanaListados")
        ventanaListados.resize(1300, 900)
        self.centralwidget = QtWidgets.QWidget(ventanaListados)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(90, 90, 1151, 451))
        self.tabla.setMinimumSize(QtCore.QSize(0, 451))
        self.tabla.setMaximumSize(QtCore.QSize(16777215, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabla.setFont(font)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(13)
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(12, item)
        self.separador1 = QtWidgets.QFrame(self.centralwidget)
        self.separador1.setGeometry(QtCore.QRect(20, 40, 481, 20))
        self.separador1.setFrameShape(QtWidgets.QFrame.HLine)
        self.separador1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separador1.setObjectName("separador1")
        self.separador2 = QtWidgets.QFrame(self.centralwidget)
        self.separador2.setGeometry(QtCore.QRect(800, 40, 461, 20))
        self.separador2.setFrameShape(QtWidgets.QFrame.HLine)
        self.separador2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separador2.setObjectName("separador2")
        self.etq_principal = QtWidgets.QLabel(self.centralwidget)
        self.etq_principal.setGeometry(QtCore.QRect(500, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etq_principal.setFont(font)
        self.etq_principal.setFrameShape(QtWidgets.QFrame.Panel)
        self.etq_principal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.etq_principal.setObjectName("etq_principal")
        self.etq_informativa = QtWidgets.QLabel(self.centralwidget)
        self.etq_informativa.setGeometry(QtCore.QRect(240, 690, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_informativa.setFont(font)
        self.etq_informativa.setObjectName("etq_informativa")
        self.visor_imagen = QtWidgets.QLabel(self.centralwidget)
        self.visor_imagen.setGeometry(QtCore.QRect(670, 590, 300, 250))
        self.visor_imagen.setFrameShape(QtWidgets.QFrame.Panel)
        self.visor_imagen.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.visor_imagen.setLineWidth(3)
        self.visor_imagen.setText("")
        self.visor_imagen.setObjectName("visor_imagen")
        ventanaListados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventanaListados)
        self.statusbar.setObjectName("statusbar")
        ventanaListados.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaListados)
        QtCore.QMetaObject.connectSlotsByName(ventanaListados)

    def retranslateUi(self, ventanaListados):
        _translate = QtCore.QCoreApplication.translate
        ventanaListados.setWindowTitle(_translate("ventanaListados", "Tabla de productos"))
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("ventanaListados", "Referencia"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("ventanaListados", "Nombre"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("ventanaListados", "Tipo"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("ventanaListados", "Escala"))
        item = self.tabla.horizontalHeaderItem(4)
        item.setText(_translate("ventanaListados", "Fabricante"))
        item = self.tabla.horizontalHeaderItem(5)
        item.setText(_translate("ventanaListados", "Precio"))
        item = self.tabla.horizontalHeaderItem(6)
        item.setText(_translate("ventanaListados", "Stock"))
        item = self.tabla.horizontalHeaderItem(7)
        item.setText(_translate("ventanaListados", "Tecnología"))
        item = self.tabla.horizontalHeaderItem(8)
        item.setText(_translate("ventanaListados", "Descripción"))
        self.etq_principal.setText(_translate("ventanaListados", "     TABLA DE PRODUCTOS"))
        self.etq_informativa.setText(_translate("ventanaListados", "Pincha en el icono para ver aquí  la imagen:"))
