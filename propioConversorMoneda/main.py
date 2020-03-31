'''
Conversor de monedas. Módulo principal

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_Conversor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import sys

def convertir ():
    cantidad = ui.EditCantidad.text()
    cantidad = str(cantidad)
    #comprobamos que no tengamos de entrada alguna coma en vez de punto o que el campo esté vacío o que no sea un número
    if cantidad =="" or cantidad.isspace() or cantidad.isalpha() or cantidad.find(",") != -1:
        mensaje = QMessageBox ()
        mensaje.setWindowTitle ("Error")
        mensaje.setText("No ha introducido un valor válido en el campo Cantidad. El decimal se representa por .")
        x = mensaje.exec_()
    else:                                                
        cantidad = float(cantidad)
        if ui.comboDivisa.currentText()=="Corona checa":
            resultado = round ((cantidad * 27.33),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Corona danesa":
            resultado = round ((cantidad * 7.47),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Corona islandesa":
            resultado = round((cantidad * 154.29),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Corona noruega":
            resultado = round((cantidad * 11.71),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Corona sueca":
            resultado = round((cantidad * 11.04),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Denar macedonio":
            resultado = round((cantidad * 0.016),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Dinar serbio":
            resultado = round ((cantidad * 117.55),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Dólar estadounidense":
            resultado = round ((cantidad * 0.90),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Dram armenio":
            resultado = round ((cantidad * 544.66),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Florín húngaro":
            resultado = round ((cantidad * 357.40),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Franco suizo":
            resultado = round ((cantidad * 0.94),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Grivna ucraniano":
            resultado = round ((cantidad * 30.71),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Kuna croata":
            resultado = round ((cantidad * 7.62),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Lari georgiano":
            resultado = round ((cantidad * 3.67),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Lek albanés":
            resultado = round ((cantidad * 128.62),2)
            ui.EditResultado.setText(str(resultado))  
        elif ui.comboDivisa.currentText()=="Leu moldavo":
            resultado = round ((cantidad * 19.86),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Leu rumano":
            resultado = round ((cantidad * 4.83),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Lev búlgaro":
            resultado = round ((cantidad * 1.96),2)
            ui.EditResultado.setText(str(resultado))    
        elif ui.comboDivisa.currentText()=="Libra esterlina":
            resultado = round ((cantidad * 0.89),2)
            ui.EditResultado.setText(str(resultado))  
        elif ui.comboDivisa.currentText()=="Lira turca":
            resultado = round ((cantidad * 7.21),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Manat azerí (Azerbaiyán)":
            resultado = round ((cantidad * 1.88),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Marco bosnioherzegovino":
            resultado = round ((cantidad * 1.95),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Rublo bieloruso":
            resultado = round ((cantidad * 2.83),2)
            ui.EditResultado.setText(str(resultado))
        elif ui.comboDivisa.currentText()=="Rublo ruso":
            resultado = round ((cantidad * 88.19),2)
            ui.EditResultado.setText(str(resultado))  
        elif ui.comboDivisa.currentText()=="Tenge kazajo":
            resultado = round ((cantidad * 489.53),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Yen japonés":
            resultado = round ((cantidad * 119.29),2)
            ui.EditResultado.setText(str(resultado)) 
        elif ui.comboDivisa.currentText()=="Zloty polaco":
            resultado = round ((cantidad * 4.54),2)
            ui.EditResultado.setText(str(resultado)) 


monedas = ["Corona checa","Corona danesa","Corona islandesa", "Corona noruega", "Corona sueca", 
           "Denar macedonio","Dinar serbio","Dólar estadounidense", "Dram armenio",  
           "Florín húngaro","Franco suizo","Grivna ucraniano","Kuna croata",
           "Lari georgiano","Lek albanés","Leu moldavo","Leu rumano","Lev búlgaro","Libra esterlina","Lira turca",
           "Manat azerí (Azerbaiyán)","Marco bosnioherzegovino",
           "Rublo bieloruso","Rublo ruso","Tenge kazajo","Yen japonés","Zloty polaco"]

paises = ["RepublicaCheca.png","Dinamarca.png","Islandia.png","Noruega.png","Suecia.png",
          "Macedonia.png","Serbia.png","USA.png","Armenia.png",
          "Hungria.png","Suiza.png","Ucrania.png","Croacia.png",
          "Georgia.png","Albania.png","Moldavia.png","Rumania.png","Bulgaria.png","ReinoUnido.png","Turquia.png",
          "Azerbaiyan.png","Bosnia.png",
          "Bielorusia.png","Rusia.png","Kazajistan.png","Japon.png","Polonia.png"]


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_Conversor.Ui_MainWindow()
ui.setupUi(MainWindow)


for m in range (len(monedas)):
    ui.comboDivisa.addItem(monedas[m])
    ui.comboDivisa.setItemIcon(m,QIcon(paises[m]))

ui.botonCalcular.clicked.connect(convertir)

MainWindow.show()
sys.exit(app.exec_())
