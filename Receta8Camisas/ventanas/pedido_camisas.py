# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pedido_camisas.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_pedido(object):
    def setupUi(self, ventana_pedido):
        ventana_pedido.setObjectName("ventana_pedido")
        ventana_pedido.resize(552, 901)
        self.etq_talla = QtWidgets.QLabel(ventana_pedido)
        self.etq_talla.setGeometry(QtCore.QRect(40, 90, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_talla.setFont(font)
        self.etq_talla.setObjectName("etq_talla")
        self.etq_pago = QtWidgets.QLabel(ventana_pedido)
        self.etq_pago.setGeometry(QtCore.QRect(30, 450, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etq_pago.setFont(font)
        self.etq_pago.setObjectName("etq_pago")
        self.etq_pedido = QtWidgets.QLabel(ventana_pedido)
        self.etq_pedido.setGeometry(QtCore.QRect(30, 800, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.etq_pedido.setFont(font)
        self.etq_pedido.setText("")
        self.etq_pedido.setObjectName("etq_pedido")
        self.etq_presentacion = QtWidgets.QLabel(ventana_pedido)
        self.etq_presentacion.setGeometry(QtCore.QRect(30, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.etq_presentacion.setFont(font)
        self.etq_presentacion.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.etq_presentacion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.etq_presentacion.setObjectName("etq_presentacion")
        self.verticalLayoutWidget = QtWidgets.QWidget(ventana_pedido)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 321, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_XS = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_XS.setFont(font)
        self.radio_XS.setObjectName("radio_XS")
        self.verticalLayout.addWidget(self.radio_XS)
        self.radio_S = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_S.setFont(font)
        self.radio_S.setObjectName("radio_S")
        self.verticalLayout.addWidget(self.radio_S)
        self.radio_M = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_M.setObjectName("radio_M")
        self.verticalLayout.addWidget(self.radio_M)
        self.radio_L = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_L.setFont(font)
        self.radio_L.setObjectName("radio_L")
        self.verticalLayout.addWidget(self.radio_L)
        self.radio_XL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_XL.setFont(font)
        self.radio_XL.setObjectName("radio_XL")
        self.verticalLayout.addWidget(self.radio_XL)
        self.radio_2XL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_2XL.setFont(font)
        self.radio_2XL.setObjectName("radio_2XL")
        self.verticalLayout.addWidget(self.radio_2XL)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(ventana_pedido)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 480, 321, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_efectivo = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_efectivo.setFont(font)
        self.radio_efectivo.setObjectName("radio_efectivo")
        self.verticalLayout_2.addWidget(self.radio_efectivo)
        self.radio_credito = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_credito.setFont(font)
        self.radio_credito.setObjectName("radio_credito")
        self.verticalLayout_2.addWidget(self.radio_credito)
        self.radio_debito = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_debito.setFont(font)
        self.radio_debito.setObjectName("radio_debito")
        self.verticalLayout_2.addWidget(self.radio_debito)
        self.radio_transferencia = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_transferencia.setFont(font)
        self.radio_transferencia.setObjectName("radio_transferencia")
        self.verticalLayout_2.addWidget(self.radio_transferencia)
        self.radio_PayPal = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_PayPal.setFont(font)
        self.radio_PayPal.setObjectName("radio_PayPal")
        self.verticalLayout_2.addWidget(self.radio_PayPal)
        self.radio_NFC = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_NFC.setFont(font)
        self.radio_NFC.setObjectName("radio_NFC")
        self.verticalLayout_2.addWidget(self.radio_NFC)

        self.retranslateUi(ventana_pedido)
        QtCore.QMetaObject.connectSlotsByName(ventana_pedido)

    def retranslateUi(self, ventana_pedido):
        _translate = QtCore.QCoreApplication.translate
        ventana_pedido.setWindowTitle(_translate("ventana_pedido", "Pedido camisas"))
        self.etq_talla.setText(_translate("ventana_pedido", "Escoge la talla de la camisa:"))
        self.etq_pago.setText(_translate("ventana_pedido", "Selecciona el método de pago:"))
        self.etq_presentacion.setText(_translate("ventana_pedido", "    PEDIDO DE CAMISAS"))
        self.radio_XS.setText(_translate("ventana_pedido", "XS"))
        self.radio_S.setText(_translate("ventana_pedido", "S"))
        self.radio_M.setText(_translate("ventana_pedido", "M"))
        self.radio_L.setText(_translate("ventana_pedido", "L"))
        self.radio_XL.setText(_translate("ventana_pedido", "XL"))
        self.radio_2XL.setText(_translate("ventana_pedido", "2XL"))
        self.radio_efectivo.setText(_translate("ventana_pedido", "Efectivo"))
        self.radio_credito.setText(_translate("ventana_pedido", "Tarjeta de crédito"))
        self.radio_debito.setText(_translate("ventana_pedido", "Tarjeta de débito"))
        self.radio_transferencia.setText(_translate("ventana_pedido", "Transferencia bancaria"))
        self.radio_PayPal.setText(_translate("ventana_pedido", "PayPal"))
        self.radio_NFC.setText(_translate("ventana_pedido", "NFC (pago por móvil)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_pedido = QtWidgets.QDialog()
    ui = Ui_ventana_pedido()
    ui.setupUi(ventana_pedido)
    ventana_pedido.show()
    sys.exit(app.exec_())
