# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bienvenida.setGeometry(QtCore.QRect(110, 220, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_bienvenida.setFont(font)
        self.lbl_bienvenida.setObjectName("lbl_bienvenida")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuRevistas = QtWidgets.QMenu(self.menubar)
        self.menuRevistas.setObjectName("menuRevistas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_registrar_revista = QtWidgets.QAction(MainWindow)
        self.submenu_registrar_revista.setObjectName("submenu_registrar_revista")
        self.submenu_listar_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_listar_revistas.setObjectName("submenu_listar_revistas")
        self.submenu_list_widget_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_list_widget_revistas.setObjectName("submenu_list_widget_revistas")
        self.submenu_table_widget_revistas = QtWidgets.QAction(MainWindow)
        self.submenu_table_widget_revistas.setObjectName("submenu_table_widget_revistas")
        self.menuRevistas.addAction(self.submenu_registrar_revista)
        self.menuRevistas.addAction(self.submenu_listar_revistas)
        self.menuRevistas.addAction(self.submenu_list_widget_revistas)
        self.menuRevistas.addAction(self.submenu_table_widget_revistas)
        self.menubar.addAction(self.menuRevistas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APLICACION GESTIÓN REVISTAS"))
        self.lbl_bienvenida.setText(_translate("MainWindow", "Bienvenido a la aplicación de gestión de revistas usando PyQt5"))
        self.menuRevistas.setTitle(_translate("MainWindow", "Revistas"))
        self.submenu_registrar_revista.setText(_translate("MainWindow", "Registrar revista"))
        self.submenu_listar_revistas.setText(_translate("MainWindow", "Listar revistas"))
        self.submenu_list_widget_revistas.setText(_translate("MainWindow", "Listar List Widget"))
        self.submenu_table_widget_revistas.setText(_translate("MainWindow", "Listar Table Widget"))
