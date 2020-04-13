'''
Aplicación de signals y Slots - Copiar y pegar

'''
from PyQt5.QtWidgets import QDialog, QApplication
from ventanas import ventana_copiar_pegar
import sys

class VentanaCopiarPegar (QDialog):
    def __init__(self):
        super().__init__() #invocamos al constructor de la clase padre QDialog.
        v_copiar_pegar = ventana_copiar_pegar.Ui_ventanaCopiarPegar()
        v_copiar_pegar.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_copiar_pegar = VentanaCopiarPegar()
    v_copiar_pegar.show()
    
    sys.exit (app.exec_())