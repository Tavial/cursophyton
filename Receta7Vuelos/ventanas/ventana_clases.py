# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_clases.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaClaseVuelo(object):
    def setupUi(self, VentanaClaseVuelo):
        VentanaClaseVuelo.setObjectName("VentanaClaseVuelo")
        VentanaClaseVuelo.resize(408, 491)
        self.etq_escoger = QtWidgets.QLabel(VentanaClaseVuelo)
        self.etq_escoger.setGeometry(QtCore.QRect(40, 110, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etq_escoger.setFont(font)
        self.etq_escoger.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.etq_escoger.setObjectName("etq_escoger")
        self.radio_business = QtWidgets.QRadioButton(VentanaClaseVuelo)
        self.radio_business.setGeometry(QtCore.QRect(40, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_business.setFont(font)
        self.radio_business.setObjectName("radio_business")
        self.etq_principal = QtWidgets.QLabel(VentanaClaseVuelo)
        self.etq_principal.setGeometry(QtCore.QRect(30, 30, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.etq_principal.setFont(font)
        self.etq_principal.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.etq_principal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.etq_principal.setObjectName("etq_principal")
        self.radio_turista_premium = QtWidgets.QRadioButton(VentanaClaseVuelo)
        self.radio_turista_premium.setGeometry(QtCore.QRect(40, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_turista_premium.setFont(font)
        self.radio_turista_premium.setObjectName("radio_turista_premium")
        self.radio_turista = QtWidgets.QRadioButton(VentanaClaseVuelo)
        self.radio_turista.setGeometry(QtCore.QRect(40, 240, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_turista.setFont(font)
        self.radio_turista.setObjectName("radio_turista")
        self.etq_resultado = QtWidgets.QLabel(VentanaClaseVuelo)
        self.etq_resultado.setGeometry(QtCore.QRect(50, 350, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.etq_resultado.setFont(font)
        self.etq_resultado.setText("")
        self.etq_resultado.setObjectName("etq_resultado")

        self.retranslateUi(VentanaClaseVuelo)
        QtCore.QMetaObject.connectSlotsByName(VentanaClaseVuelo)

    def retranslateUi(self, VentanaClaseVuelo):
        _translate = QtCore.QCoreApplication.translate
        VentanaClaseVuelo.setWindowTitle(_translate("VentanaClaseVuelo", "Clase del vuelo"))
        self.etq_escoger.setText(_translate("VentanaClaseVuelo", "Escoge la clase del vuelo: "))
        self.radio_business.setText(_translate("VentanaClaseVuelo", "Business Flexible -  5989 €"))
        self.etq_principal.setText(_translate("VentanaClaseVuelo", "  Vuelo Madrid - Toronto"))
        self.radio_turista_premium.setText(_translate("VentanaClaseVuelo", "Turista Premium Flexible -  2564 €"))
        self.radio_turista.setText(_translate("VentanaClaseVuelo", "Turista Flexible -  2250 €"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaClaseVuelo = QtWidgets.QDialog()
    ui = Ui_VentanaClaseVuelo()
    ui.setupUi(VentanaClaseVuelo)
    VentanaClaseVuelo.show()
    sys.exit(app.exec_())
