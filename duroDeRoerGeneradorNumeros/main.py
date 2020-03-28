'''
Módulo principal del generador de números gráfico

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_generador
from PyQt5.QtWidgets import QMessageBox
import sys, random

def generarAleatorio():
    # obtenemos strings. Hay que pasarlos a entero
    numero1 = int (ui.spinNumero1.value()) 
    numero2 = int (ui.spinNumero2.value())
    
    if numero1 > numero2: 
        mensaje = QMessageBox ()
        mensaje.setWindowTitle ("Error")
        mensaje.setText("El número 1 es mayor que el número 2. Tiene que ser menor o igual")
        x = mensaje.exec_()
    else:
        # el entero obtenido tras el random hay que pasarlo a cadena para poder mostrarlo en el textBox
        aleatorio = str (random.randint (numero1,numero2))
        ui.textGenerado.setText(aleatorio)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_generador.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.botonGenerar.clicked.connect(generarAleatorio)

MainWindow.show()
sys.exit(app.exec_())