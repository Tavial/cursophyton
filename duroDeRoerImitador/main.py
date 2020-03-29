'''
Módulo principal del imitador (espejo). Vamos a crear un imitador, como si fuera 
un espejo. Tendremos dos pares de conjunto de elementos separados (puedes usar 
un separador) y cuando nosotros pinchamos en un elemento o escribimos en un 
campo, se debe cambiar el otro lado.

Por ejemplo, si yo tengo un campo de texto y escribo en él, el campo de texto 
que es su reflejo también recibirá ese texto.

Solo se puede modificar de un lado, el otro conjunto no lo podemos modificar, es 
decir, que no es bidireccional.

'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_imitador
import sys

def imitador():
    # Controlamos la pulsación en los radioButtons    
    if ui.radioOpcion1_original.isChecked():
        ui.radioOpcion1_espejo.setChecked(True)
    elif ui.radioOpcion2_original.isChecked():
        ui.radioOpcion2_espejo.setChecked(True)
    elif ui.radioOpcion3_original.isChecked():
        ui.radioOpcion3_espejo.setChecked(True)
    
    # Controlamos la pulsación en los checkBox  
    if ui.checkOpcion4_original.isChecked():
        ui.checkOpcion4_espejo.setChecked(True)
    else:
        ui.checkOpcion4_espejo.setChecked(False)
        
    if ui.checkOpcion5_original.isChecked():
        ui.checkOpcion5_espejo.setChecked(True)
    else:
        ui.checkOpcion5_espejo.setChecked(False)
     
    if ui.checkOpcion6_original.isChecked():
        ui.checkOpcion6_espejo.setChecked(True)
    else:
        ui.checkOpcion6_espejo.setChecked(False)
    
    # Controlamos el cambio de valor del spinBox. Pasamos el valor del original al espejo
    ui.spinEspejo.setValue (ui.spinOriginal.value())
  
    # Controlamos el cambio de valor del lineEdit. Fijamos el valor del original al espejo
    ui.editEspejo.setText(ui.editOriginal.text())
    
    # Controlamos el cambio de valor del ComboBox. Fijamos el valor del original al espejo
    ui.comboEspejo.setCurrentText(ui.comboOriginal.currentText())


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
    
ui = ventana_imitador.Ui_MainWindow()
ui.setupUi(MainWindow)

frutas = ["manzana","sandía","naranja","kiwi","plátano","ciruela"]

for f in frutas:
    ui.comboOriginal.addItem(f)
    ui.comboEspejo.addItem(f)

#Controlamos el evento de pulsar los botones de los radioButtons
ui.radioOpcion1_original.clicked.connect(imitador)
ui.radioOpcion2_original.clicked.connect(imitador)
ui.radioOpcion3_original.clicked.connect(imitador)

#Controlamos el evento de pulsar los botones de los CheckBox
ui.checkOpcion4_original.clicked.connect(imitador)
ui.checkOpcion5_original.clicked.connect(imitador)
ui.checkOpcion6_original.clicked.connect(imitador)

#Controlamos el evento de cambiar el valor del SpinBox
ui.spinOriginal.valueChanged.connect(imitador)

#Controlamos el evento de cambiar el valor del LineEdit
ui.editOriginal.textChanged.connect(imitador)

#Controlamos el evento de cambiar el valor del ComboBox
ui.comboOriginal.currentTextChanged.connect(imitador)







MainWindow.show()


sys.exit(app.exec_())