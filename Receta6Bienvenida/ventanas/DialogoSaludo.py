# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoSaludo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bienvenida(object):
    def setupUi(self, Bienvenida):
        Bienvenida.setObjectName("Bienvenida")
        Bienvenida.resize(633, 268)
        Bienvenida.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.etq_nombre = QtWidgets.QLabel(Bienvenida)
        self.etq_nombre.setGeometry(QtCore.QRect(30, 50, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_nombre.setFont(font)
        self.etq_nombre.setObjectName("etq_nombre")
        self.etq_saludo = QtWidgets.QLabel(Bienvenida)
        self.etq_saludo.setGeometry(QtCore.QRect(30, 110, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_saludo.setFont(font)
        self.etq_saludo.setObjectName("etq_saludo")
        self.etq_resultado = QtWidgets.QLabel(Bienvenida)
        self.etq_resultado.setGeometry(QtCore.QRect(240, 100, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.etq_resultado.setFont(font)
        self.etq_resultado.setText("")
        self.etq_resultado.setObjectName("etq_resultado")
        self.texto_nombre = QtWidgets.QLineEdit(Bienvenida)
        self.texto_nombre.setGeometry(QtCore.QRect(220, 40, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.texto_nombre.setFont(font)
        self.texto_nombre.setObjectName("texto_nombre")
        self.boton_saludar = QtWidgets.QPushButton(Bienvenida)
        self.boton_saludar.setGeometry(QtCore.QRect(220, 170, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_saludar.setFont(font)
        self.boton_saludar.setObjectName("boton_saludar")

        self.retranslateUi(Bienvenida)
        QtCore.QMetaObject.connectSlotsByName(Bienvenida)

    def retranslateUi(self, Bienvenida):
        _translate = QtCore.QCoreApplication.translate
        Bienvenida.setWindowTitle(_translate("Bienvenida", "Saludar"))
        self.etq_nombre.setText(_translate("Bienvenida", "Introduce tu nombre: "))
        self.etq_saludo.setText(_translate("Bienvenida", "Saludo:"))
        self.boton_saludar.setText(_translate("Bienvenida", "Saludar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bienvenida = QtWidgets.QDialog()
    ui = Ui_Bienvenida()
    ui.setupUi(Bienvenida)
    Bienvenida.show()
    sys.exit(app.exec_())
