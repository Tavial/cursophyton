'''
Módulo principal. Saludador configurable

'''

import sys
from ventanas import ventana_saludador
from PyQt5 import QtCore, QtGui, QtWidgets

def saludar():
    nom = ui.nombre.text()
    ui.etq_resultado.setText ("Hola "+nom)
 

#línea obligatoria para usar pyqt5
app = QtWidgets.QApplication(sys.argv)

#se prepara un MainWindow de pyqt5, esta sería parte del código recomendado de pyqt5
MainWindow = QtWidgets.QMainWindow()

#así crea un objeto de la clase en el archivo generado y lo usa para preparar la ventana principal
#llamada MainWindow para que tenga todo lo que pusimos en el designer    
ui = ventana_saludador.Ui_MainWindow()

# todos los componentes puestos de la ventana por el designer están en ui
ui.setupUi(MainWindow)

#programamos el boton
ui.boton_saludo.clicked.connect(saludar)
## ui.pushButton.clicked.connect(transformar_a_dolares)

MainWindow.show()
sys.exit(app.exec_())