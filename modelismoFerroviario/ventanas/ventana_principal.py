# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(1300, 900)
        self.centralwidget = QtWidgets.QWidget(ventanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_titulo = QtWidgets.QLabel(self.centralwidget)
        self.etq_titulo.setGeometry(QtCore.QRect(40, 200, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.etq_titulo.setFont(font)
        self.etq_titulo.setObjectName("etq_titulo")
        ventanaPrincipal.setCentralWidget(self.centralwidget)
        self.Menu = QtWidgets.QMenuBar(ventanaPrincipal)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 1300, 38))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Menu.setFont(font)
        self.Menu.setObjectName("Menu")
        self.menuProductos = QtWidgets.QMenu(self.Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.menuProductos.setFont(font)
        self.menuProductos.setObjectName("menuProductos")
        self.menuListar_productos = QtWidgets.QMenu(self.menuProductos)
        self.menuListar_productos.setObjectName("menuListar_productos")
        ventanaPrincipal.setMenuBar(self.Menu)
        self.statusbar = QtWidgets.QStatusBar(ventanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        ventanaPrincipal.setStatusBar(self.statusbar)
        self.submenu_nuevo_producto = QtWidgets.QAction(ventanaPrincipal)
        self.submenu_nuevo_producto.setObjectName("submenu_nuevo_producto")
        self.accion_listar_lista = QtWidgets.QAction(ventanaPrincipal)
        self.accion_listar_lista.setObjectName("accion_listar_lista")
        self.accion_listar_tabla = QtWidgets.QAction(ventanaPrincipal)
        self.accion_listar_tabla.setObjectName("accion_listar_tabla")
        self.menuListar_productos.addAction(self.accion_listar_lista)
        self.menuListar_productos.addSeparator()
        self.menuListar_productos.addAction(self.accion_listar_tabla)
        self.menuProductos.addAction(self.submenu_nuevo_producto)
        self.menuProductos.addSeparator()
        self.menuProductos.addAction(self.menuListar_productos.menuAction())
        self.Menu.addAction(self.menuProductos.menuAction())

        self.retranslateUi(ventanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Modelismo ferroviario"))
        self.etq_titulo.setText(_translate("ventanaPrincipal", "MODELISMO FERROVIARIO"))
        self.menuProductos.setTitle(_translate("ventanaPrincipal", "Productos"))
        self.menuListar_productos.setTitle(_translate("ventanaPrincipal", "Listar productos"))
        self.submenu_nuevo_producto.setText(_translate("ventanaPrincipal", "Nuevo producto"))
        self.accion_listar_lista.setText(_translate("ventanaPrincipal", "Listado"))
        self.accion_listar_tabla.setText(_translate("ventanaPrincipal", "Tabla"))
