'''
Manejo de Radio Buttons - Escoger la clase de un vuelo Madrid-Toronto

'''

from PyQt5.QtWidgets import QDialog, QApplication
from ventanas import ventana_clases
import sys


class ClaseVuelo (QDialog): # Definimos la clase ClaseVuelo que hereda de QDialog
    def __init__(self): # Definimos el constructor de nuestra Clase Vuelo
        super().__init__() # invocamos al constructor de la clase padre QDialog
        #creamos una instancia de la clase Ui_VentanaClaseVuelo que está en el módulo ventana_clases en el paquete ventanas
        self.clase = ventana_clases.Ui_VentanaClaseVuelo()
        #inicializamos el interface donde tenemos los componentes (radio buttons, labels...)
        self.clase.setupUi(self)
        # capturamos los eventos de los botones
        self.clase.radio_business.clicked.connect (self.escogeClase)
        self.clase.radio_turista_premium.clicked.connect (self.escogeClase)
        self.clase.radio_turista.clicked.connect (self.escogeClase)
        # mostramos 
        self.show()
    
    def escogeClase(self):    
        if self.clase.radio_business.isChecked():
            clase_escogida = self.clase.radio_business.text()
        elif self.clase.radio_turista_premium.isChecked():
            clase_escogida = self.clase.radio_turista_premium.text()
        elif self.clase.radio_turista.isChecked():
            clase_escogida = self.clase.radio_turista.text()
            
        self.clase.etq_resultado.setText (clase_escogida) #muestra la opción escogida en la etq_resultado

if __name__ == "__main__":
    #definimos instancia de la clase QApplication
    app = QApplication (sys.argv)
    #definimos instancia de la clase que hemos creado ClaseVuelo
    clase = ClaseVuelo()
    #mostramos nuestro diálogo ClaseVuelo
    clase.show()
    #método de salida
    sys.exit (app.exec_())