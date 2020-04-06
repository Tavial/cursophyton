'''
PIZZERIA - Uso de CheckBoxes

'''
from PyQt5.QtWidgets import QDialog,QApplication
from ventanas import ventana_pizzeria
import sys

class VentanaPizzeria (QDialog):
    
    
      
    def __init__(self): # implementamos el método constructor de la clase
        self.importe_total = 12.20
        self.seleccionados = [False,False,False,False,False,False,False,False,False]
        super().__init__() # llamamos al método constructor de la clase padre QDialog 
        self.v_pizzeria = ventana_pizzeria.Ui_ventanaDialogo () # creamos un objeto de la clase Ui_ventanaDialogo del paquete ventanas
        self.v_pizzeria.setupUi(self) # inicializamos el interface de la ventana (donde se muestran los componentes gráficos)
        # capturamos los eventos del click de ratón
        self.v_pizzeria.check_aceitunas.clicked.connect(self.escogerComplemento)
        self.v_pizzeria.check_atun.clicked.connect(self.escogerComplemento)
        self.v_pizzeria.check_bacon.clicked.connect(self.escogerComplemento)
        self.v_pizzeria.check_cebolla.clicked.connect(self.escogerComplemento)
        self.v_pizzeria.check_champis.clicked.connect (self.escogerComplemento)
        self.v_pizzeria.check_jamon.clicked.connect (self.escogerComplemento)
        self.v_pizzeria.check_pepperoni.clicked.connect (self.escogerComplemento)
        self.v_pizzeria.check_pollo.clicked.connect (self.escogerComplemento)
        self.v_pizzeria.check_york.clicked.connect (self.escogerComplemento)
        
        
    def escogerComplemento(self):
        
        # ACEITUNAS
        
        if self.v_pizzeria.check_aceitunas.isChecked() : # si seleccionamos aceitunas
            if not self.seleccionados[0]: # si no estaban seleccionadas
                self.seleccionados[0] = True # las marcamos como seleccionadas...
                self.importe_total += 1.95 # ... aumentamos al precio total el coste de las aceitunas
            # si ya estaban seleccionadas las aceitunas lo dejamos tal como está sin aumentarle precio ni cambiar el estado
        else: # si deseleccionamos aceitunas
            if self.seleccionados[0]: # si estaban seleccionadas
                self.seleccionados[0] = False # las desmarcamos como seleccionadas...
                self.importe_total -= 1.95 # ... restamos al precio total el coste de las aceitunas
            # si no estaban seleccionadas las aceitunas lo dejamos tal como está sin disminuir precio ni cambiar el estado
            
        # Hacemos lo anterior para cada complemento        
            
        # ATUN
        
        if self.v_pizzeria.check_atun.isChecked() :
            if not self.seleccionados[1]:
                self.seleccionados[1] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[1]: 
                self.seleccionados[1] = False 
                self.importe_total -= 1.95 
                
                
        # BACON
        
        if self.v_pizzeria.check_bacon.isChecked() :
            if not self.seleccionados[2]:
                self.seleccionados[2] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[2]: 
                self.seleccionados[2] = False 
                self.importe_total -= 1.95 
                
                
        # CEBOLLA
        
        if self.v_pizzeria.check_cebolla.isChecked() :
            if not self.seleccionados[3]:
                self.seleccionados[3] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[3]: 
                self.seleccionados[3] = False 
                self.importe_total -= 1.95 
                
                
        # CHAMPIÑONES
        
        if self.v_pizzeria.check_champis.isChecked() :
            if not self.seleccionados[4]:
                self.seleccionados[4] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[4]: 
                self.seleccionados[4] = False 
                self.importe_total -= 1.95 
                
                
        # JAMON SERRANO
        
        if self.v_pizzeria.check_jamon.isChecked() :
            if not self.seleccionados[5]:
                self.seleccionados[5] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[5]: 
                self.seleccionados[5] = False 
                self.importe_total -= 1.95 
                
        # PEPPERONI
        
        if self.v_pizzeria.check_pepperoni.isChecked() :
            if not self.seleccionados[6]:
                self.seleccionados[6] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[6]: 
                self.seleccionados[6] = False 
                self.importe_total -= 1.95 
        
        
        # POLLO
        
        if self.v_pizzeria.check_pollo.isChecked() :
            if not self.seleccionados[7]:
                self.seleccionados[7] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[7]: 
                self.seleccionados[7] = False 
                self.importe_total -= 1.95 
                
                
        # YORK
        
        if self.v_pizzeria.check_york.isChecked() :
            if not self.seleccionados[8]:
                self.seleccionados[8] = True 
                self.importe_total += 1.95 
           
        else:
            if self.seleccionados[8]: 
                self.seleccionados[8] = False 
                self.importe_total -= 1.95 
        importe = round (self.importe_total,2)
        self.v_pizzeria.etq_precio_final.setText(str(importe)+" €")
        
if __name__=="__main__":
    # creamos una instancia de la clase aplicación
    app = QApplication (sys.argv)
    # creamos un objeto de nuestra clase VentanaPizzeria
    v_pizzeria = VentanaPizzeria()
    # mostramos la ventana
    v_pizzeria.show()
    # método de salida
    sys.exit(app.exec_())

