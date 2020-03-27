# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_peliculas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 472)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.etq_titulo = QtWidgets.QLabel(self.centralwidget)
        self.etq_titulo.setGeometry(QtCore.QRect(50, 100, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.etq_titulo.setFont(font)
        self.etq_titulo.setObjectName("etq_titulo")
        self.etq_peliculas = QtWidgets.QLabel(self.centralwidget)
        self.etq_peliculas.setGeometry(QtCore.QRect(460, 100, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.etq_peliculas.setFont(font)
        self.etq_peliculas.setObjectName("etq_peliculas")
        self.edit_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_titulo.setGeometry(QtCore.QRect(50, 140, 311, 31))
        self.edit_titulo.setObjectName("edit_titulo")
        self.combo_peliculas = QtWidgets.QComboBox(self.centralwidget)
        self.combo_peliculas.setGeometry(QtCore.QRect(460, 140, 371, 31))
        self.combo_peliculas.setObjectName("combo_peliculas")
        self.boton_pelicula = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pelicula.setGeometry(QtCore.QRect(50, 240, 171, 41))
        self.boton_pelicula.setObjectName("boton_pelicula")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Películas"))
        self.etq_titulo.setText(_translate("MainWindow", "Escribe el título de una película"))
        self.etq_peliculas.setText(_translate("MainWindow", "Películas"))
        self.boton_pelicula.setText(_translate("MainWindow", "Añadir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
