# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_list_widget_revistas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_listado = QtWidgets.QLabel(self.centralwidget)
        self.etq_listado.setGeometry(QtCore.QRect(130, 40, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.etq_listado.setFont(font)
        self.etq_listado.setObjectName("etq_listado")
        self.list_widget_revistas = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget_revistas.setGeometry(QtCore.QRect(30, 120, 531, 351))
        self.list_widget_revistas.setObjectName("list_widget_revistas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.etq_listado.setText(_translate("MainWindow", "Listado usando List Widget "))
