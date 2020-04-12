# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listado_revistas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado.setGeometry(QtCore.QRect(230, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setObjectName("lbl_listado")
        self.listado_revistas = QtWidgets.QTextEdit(self.centralwidget)
        self.listado_revistas.setGeometry(QtCore.QRect(60, 90, 461, 341))
        self.listado_revistas.setObjectName("listado_revistas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listado de revistas"))
        self.lbl_listado.setText(_translate("MainWindow", "Listado revistas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
