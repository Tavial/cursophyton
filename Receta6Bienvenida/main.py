'''
Módulo principal del Mensaje de Bienvenida

'''

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
import sys
from ventanas import DialogoSaludo

class DialogoSaludoAplicacion (QDialog): # Creamos nuestra clase que hereda de QDialog
    def __init__(self): # Definimos el método constructor de nuestra clase DialogoSaludoAplicacion  
        super().__init__() # Llamamos al método constructor de la clase padre QDialog
    
        #self.dialogo equivale al ui que utilizábamos en la otra versión    
        self.dialogo = DialogoSaludo.Ui_Bienvenida ()  # instanciamos un objeto de la clase Ui_Bienvenida que está en DialogoSaludo.ui
        # inicializamos la interfaz (donde creamos las etiquetas, el botón, el edit line 
        # para ello invocamos al método setupUi (self)
        self.dialogo.setupUi(self)
        # manejador de eventos del ratón
        self.dialogo.boton_saludar.clicked.connect(self.mostrarSaludo)
        
        self.show() 
    
    def mostrarSaludo(self):     
        mensaje = self.dialogo.texto_nombre.text()  
        validar = str(mensaje)
        if validar =="" or validar.isspace():
            error = QMessageBox ()
            error.setWindowTitle ("Error")
            error.setText(" Tienes que introducir algún valor en el nombre")
            x = error.exec_()
        else:
            self.dialogo.etq_resultado.setText("Hola, "+mensaje)
        
if __name__ == "__main__":
    # creamos instancia de QApplication. Creo el entorno
    app = QApplication(sys.argv)
    # creo una instancia de la clase que hemos creado (objeto diálogo)
    dialogo = DialogoSaludoAplicacion()
    # Muestro el diálogo
    dialogo.show()
    # evento de salida 
    sys.exit (app.exec_())
    
    