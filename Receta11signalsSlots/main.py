'''
Aplicación con señales y slots. Borrar cuadro de edición

'''

from PyQt5.QtWidgets import QDialog, QApplication
from ventanas import ventana_borrado
import sys

class VentanaBorrado (QDialog):
    def __init__(self):
        super().__init__() # llamamos al constructor de la clase padre (QDialog)
        self.v_borrado = ventana_borrado.Ui_ventanaDialogo ()
        self.v_borrado.setupUi(self)
        
if __name__ =="__main__":
    app = QApplication (sys.argv)
    
    v_borrado = VentanaBorrado ()
    v_borrado.show()
    
    sys.exit (app.exec_())
    
        
        
        
