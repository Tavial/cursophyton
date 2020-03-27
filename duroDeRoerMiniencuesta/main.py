'''
Módulo principal de la miniencuesta

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_encuesta

import sys
from PyQt5.QtWidgets import QMessageBox

def generarResultado():
    especialidad = []
    if ui.radioWindows.isChecked():
        so = "Windows"
    elif ui.radioLinux.isChecked():
        so = "Linux"
    elif ui.radioMac.isChecked():
        so = "Mac"
    
    if ui.checkProgramacion.isChecked():
        especialidad.append("Programación")
    if ui.checkDisenyo.isChecked():
        especialidad.append("Diseño")
    if ui.checkAdministracion.isChecked():
        especialidad.append("Administración")
   
    especialidad_str = " ".join(especialidad)
    
    horas = ui.sliderHoras.value()
    
    # Una vez recogidos todos los datos los mostramos en una ventana emergente
    mensaje = QMessageBox ()
    mensaje.setWindowTitle ("Muestra de datos")
    mensaje.setText("Tu sistema preferido es: "+so+". Tus especialidades son: "+especialidad_str+" y el número de horas dedicadas al ordenador son "+str(horas))
    x = mensaje.exec_()
    
    
       
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_encuesta.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.botonGenerar.clicked.connect(generarResultado)

MainWindow.show()
sys.exit(app.exec_())