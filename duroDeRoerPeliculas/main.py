'''
Módulo principal Películas

'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_peliculas

def anadirPelicula():
    pelicula = ui.edit_titulo.text()
    ui.combo_peliculas.addItem(pelicula)
    ui.edit_titulo.setText("")
    
  
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_peliculas.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.boton_pelicula.clicked.connect(anadirPelicula)
MainWindow.show()
sys.exit(app.exec_())