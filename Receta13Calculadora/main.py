'''
Calculadora PyQt5 de valores enteros. Módulo principal

'''
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from ventanas import ventana_calculadora
import sys

class VentanaCalculadora(QDialog):
    def __init__(self):
        super ().__init__() # invocamos al constructor de la clase padre (QDialog)
        self.v_calculadora = ventana_calculadora.Ui_ventanaCalculadora()
        self.v_calculadora.setupUi(self)
        # capturamos los eventos de pulsar los botones de las operaciones
        self.v_calculadora.boton_suma.clicked.connect(self.suma)
        self.v_calculadora.boton_resta.clicked.connect(self.resta)
        self.v_calculadora.boton_producto.clicked.connect(self.producto)
        self.v_calculadora.boton_cociente.clicked.connect(self.cociente)
        
        
    def suma (self):
        correcto = self.comprobacion ()
        if not correcto:
            QMessageBox.about (self,"Error","Alguno de los campos tienen valores no válidos")
        else:
            valor1 = int (self.v_calculadora.line_primer_numero.text()) 
            valor2 = int (self.v_calculadora.line_segundo_numero.text())
            
            suma = valor1 + valor2
            
            self.v_calculadora.line_resultado.setText(str(suma))
    
    def resta (self):         
        correcto = self.comprobacion ()
        if not correcto:
            QMessageBox.about (self,"Error","Alguno de los campos tienen valores no válidos")
        else:
            valor1 = int (self.v_calculadora.line_primer_numero.text()) 
            valor2 = int (self.v_calculadora.line_segundo_numero.text())
            
            resta = valor1 - valor2
            
            self.v_calculadora.line_resultado.setText(str(resta))
    
    def producto (self):
        correcto = self.comprobacion ()
        if not correcto:
            QMessageBox.about (self,"Error","Alguno de los campos tienen valores no válidos")
        else:
            valor1 = int (self.v_calculadora.line_primer_numero.text()) 
            valor2 = int (self.v_calculadora.line_segundo_numero.text())
            
            producto = valor1 * valor2
            
            self.v_calculadora.line_resultado.setText(str(producto))
    
    def cociente (self):
        correcto = self.comprobacion ()
        if not correcto:
            QMessageBox.about (self,"Error","Alguno de los campos tienen valores no válidos")
        else:
            valor1 = int (self.v_calculadora.line_primer_numero.text()) 
            valor2 = int (self.v_calculadora.line_segundo_numero.text())
            
            cociente = valor1 // valor2
            
            self.v_calculadora.line_resultado.setText(str(cociente))
              
        
    def comprobacion (self):
        valor1 = str (self.v_calculadora.line_primer_numero.text())
        valor2 = str (self.v_calculadora.line_segundo_numero.text())
        
        if valor1 =="" or valor1.isalpha() or valor1.find(",") != -1 or valor1.find(".") != -1 \
           or valor2 =="" or valor2.isalpha() or valor2.find(",") != -1 or valor2.find(".") != -1:
            return False
        else: 
            return True
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_calculadora = VentanaCalculadora ()
    v_calculadora.show ()
    sys.exit (app.exec_())