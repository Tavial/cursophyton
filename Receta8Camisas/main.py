'''
Manejo de Check Box Agrupados - Pedido de camisas

'''
from PyQt5.QtWidgets import QDialog, QApplication
from ventanas import pedido_camisas
import sys

class VentanaPedido (QDialog): #creamos la clase pedido que hereda de la clase padre QDialog
    def __init__(self): #creamos el constructor de nuestra clase
        super().__init__() #llamamos al constructor de la clase padre.(QDialog)
        self.pedido = pedido_camisas.Ui_ventana_pedido() #Creamos una instancia de la clase que está en el paquete ventanas en el módulo pedido_camisas
        #Inicializamos el entorno (donde están nuestros radioButtons y etiquetas)
        self.pedido.setupUi(self)
        # Capturar los eventos de los radio buttons
        # Radio Buttons del contenedor (layout vertical) que agrupa los radiobuttons de la talla  
        self.pedido.radio_XS.clicked.connect (self.escoge)
        self.pedido.radio_S.clicked.connect (self.escoge)
        self.pedido.radio_M.clicked.connect (self.escoge)
        self.pedido.radio_L.clicked.connect (self.escoge)
        self.pedido.radio_XL.clicked.connect (self.escoge)
        self.pedido.radio_2XL.clicked.connect (self.escoge)
        # Radio Buttons del contenedor (layout vertical) que agrupa los radiobuttons de los medios de pago
        self.pedido.radio_efectivo.clicked.connect (self.escoge) 
        self.pedido.radio_credito.clicked.connect (self.escoge)
        self.pedido.radio_debito.clicked.connect (self.escoge)
        self.pedido.radio_transferencia.clicked.connect (self.escoge)
        self.pedido.radio_PayPal.clicked.connect (self.escoge)
        self.pedido.radio_NFC.clicked.connect (self.escoge)
    
    def escoge (self):
        talla =""
        pago =""
        if self.pedido.radio_XS.isChecked():
            talla = self.pedido.radio_XS.text()
        if self.pedido.radio_S.isChecked():
            talla = self.pedido.radio_S.text()
        if self.pedido.radio_M.isChecked():
            talla = self.pedido.radio_M.text()
        if self.pedido.radio_L.isChecked():
            talla = self.pedido.radio_L.text()
        if self.pedido.radio_XL.isChecked():
            talla = self.pedido.radio_XL.text()
        if self.pedido.radio_2XL.isChecked():
            talla = self.pedido.radio_2XL.text()     
        
        if self.pedido.radio_efectivo.isChecked():
            pago = self.pedido.radio_efectivo.text()
        if self.pedido.radio_credito.isChecked():
            pago = self.pedido.radio_credito.text()
        if self.pedido.radio_debito.isChecked():
            pago = self.pedido.radio_debito.text()
        if self.pedido.radio_transferencia.isChecked():
            pago = self.pedido.radio_transferencia.text()
        if self.pedido.radio_PayPal.isChecked():
            pago = self.pedido.radio_PayPal.text()
        if self.pedido.radio_NFC.isChecked():
            pago = self.pedido.radio_NFC.text()
        
        
        self.pedido.etq_pedido.setText("Has pedido una camisa talla "+str(talla)+" y lo vas a pagar por "+str(pago))
        
    
if __name__ == "__main__":
    #creamos un objeto de la clase QApplication
    app = QApplication(sys.argv)
    #creamos un objeto de la clase VentanaPedido
    pedido = VentanaPedido()
    #mostramos la clase
    pedido.show()
    #evento para finalizar
    sys.exit (app.exec_())
        