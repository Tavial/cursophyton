'''
HELADERIA DEL'ICE - Manejo de grupos de checkbox

'''
from PyQt5.QtWidgets import QApplication, QDialog
from ventanas import ventana_heladeria
import sys


# creamos la clase VentanaHeladeria que va a heredar de QDialog

class VentanaHeladeria (QDialog):
    # implementamos el constructor de nuestra clase
    def __init__(self):
        # invocamos al constructor de la clase padre (QDialog)
        super().__init__()
        # creamos un objeto de la clase Ui_ventanaHeladeria que es la que contiene nuestros componentes
        self.v_heladeria = ventana_heladeria.Ui_ventanaHeladeria()
        self.lista_helados = [True, False, False, False, False]
        self.lista_bebidas = [True, False, False, False, False]
        self.importe = 0
        # Ahora inicializamos el entorno de nuestros componentes 
        self.v_heladeria.setupUi(self)
        # capturamos los eventos de hacer clic en los checkbox
           
        self.v_heladeria.grupo_helados.clicked.connect (self.click_grupo_helados)
        self.v_heladeria.grupo_bebidas.clicked.connect (self.click_grupo_bebidas)
        
        self.v_heladeria.check_turron.clicked.connect (self.click_helado_turron)
        self.v_heladeria.check_muerte.clicked.connect (self.click_helado_muerteXchocolate)
        self.v_heladeria.check_after.clicked.connect (self.click_helado_after)
        self.v_heladeria.check_dama.clicked.connect (self.click_helado_dama)
        
        self.v_heladeria.check_zumo.clicked.connect (self.click_bebida_zumo)
        self.v_heladeria.check_smoothie.clicked.connect (self.click_bebida_smoothie)
        self.v_heladeria.check_chocolate.clicked.connect (self.click_bebida_chocolate)
        self.v_heladeria.check_cafe.clicked.connect (self.click_bebida_cafe)
        
    def click_grupo_helados (self):
        if self.lista_helados [0] == True: # estaba activado, por tanto con este clic se desactiva
            self.lista_helados [0] = False
            
            #...desactivamos sus casillas y no cuentan para el precio final 
            self.v_heladeria.check_turron.setChecked(False)
            if self.lista_helados [1] == True: # descontamos su precio del total
                self.importe -= 5.80
            self.lista_helados [1] = False
            
            
            self.v_heladeria.check_muerte.setChecked (False)
            if self.lista_helados [2] == True: # descontamos su precio del total
                self.importe -= 5.10
            self.lista_helados [2] = False
            
            self.v_heladeria.check_after.setChecked (False)
            if self.lista_helados [3] == True: # descontamos su precio del total
                self.importe -= 5.10
            self.lista_helados [3] = False
            
            self.v_heladeria.check_dama.setChecked (False)
            if self.lista_helados [4] == True: # descontamos su precio del total
                self.importe -= 5.20        
            self.lista_helados [4] = False
        
        else: # estaba desactivado, lo activamos
            self.lista_helados [0] = True
        imp = round ((self.importe),2) 
        self.v_heladeria.etq_importe.setText(str(imp)+" €")    
            
    def click_helado_turron (self):
        if self.lista_helados[1] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_helados [1] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 5.80
        else: # estaba desactivado por tanto lo activamos
            self.lista_helados [1] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 5.80
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
            
    def click_helado_muerteXchocolate (self):
        if self.lista_helados[2] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_helados [2] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 5.10
        else: # estaba desactivado por tanto lo activamos
            self.lista_helados [2] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 5.10
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
            
    
    def click_helado_after (self):
        if self.lista_helados[3] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_helados [3] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 5.10
        else: # estaba desactivado por tanto lo activamos
            self.lista_helados [3] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 5.10  
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €") 
            
    def click_helado_dama (self):
        if self.lista_helados[4] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_helados [4] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 5.20
        else: # estaba desactivado por tanto lo activamos
            self.lista_helados [4] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 5.20 
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")  
    
    def click_grupo_bebidas (self):
        if self.lista_bebidas [0] == True: # estaba activado, por tanto con este clic se desactiva
            self.lista_bebidas [0] = False
            #...desactivamos sus casillas y no cuentan para el precio final 
            
            self.v_heladeria.check_zumo.setChecked(False)
            if self.lista_bebidas [1] == True: # descontamos su precio del total
                self.importe -= 1.80
            self.lista_bebidas [1] = False
            
            self.v_heladeria.check_smoothie.setChecked (False)
            if self.lista_bebidas [2] == True: # descontamos su precio del total
                self.importe -= 3.50
            self.lista_bebidas [2] = False
            
            self.v_heladeria.check_chocolate.setChecked (False)
            if self.lista_bebidas [3] == True: # descontamos su precio del total
                self.importe -= 1.80
            self.lista_bebidas [3] = False
            
            self.v_heladeria.check_cafe.setChecked (False)
            if self.lista_bebidas [4] == True: # descontamos su precio del total
                self.importe -= 1.10          
            self.lista_bebidas [4] = False
        
        else: # estaba desactivado, lo activamos
            self.lista_bebidas [0] = True
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
            
    def click_bebida_zumo (self):
        if self.lista_bebidas[1] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_bebidas [1] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 1.80
        else: # estaba desactivado por tanto lo activamos
            self.lista_bebidas [1] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 1.80
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
            
    def click_bebida_smoothie (self):
        if self.lista_bebidas[2] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_bebidas [2] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 3.50
        else: # estaba desactivado por tanto lo activamos
            self.lista_bebidas [2] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 3.50
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
            
    def click_bebida_chocolate (self):
        if self.lista_bebidas[3] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_bebidas [3] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 1.80
        else: # estaba desactivado por tanto lo activamos
            self.lista_bebidas [3] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 1.80
        imp = round ((self.importe),2)
        self.v_heladeria.etq_importe.setText(str(imp)+" €")
        
    def click_bebida_cafe (self):     
        if self.lista_bebidas[4] == True: # estaba activado por tanto con este clic se desactiva
            self.lista_bebidas [4] = False
            # y como estaba activado le restamos el precio al precio total
            self.importe -= 1.10
        else: # estaba desactivado por tanto lo activamos
            self.lista_bebidas [4] = True
            # y como estaba desactivado le aumentamos el precio al precio total
            self.importe += 1.10 
        imp = round ((self.importe),2) 
        self.v_heladeria.etq_importe.setText(str(imp)+" €")  
       
if __name__ == "__main__":
    #creamos un objeto de tipo QApplication
    app = QApplication (sys.argv)
    # creamos un objeto de nuestra clase VentanaHeladeria
    v_heladeria = VentanaHeladeria ()
    # mostramos la ventana Heladeria con todos sus componentes
    v_heladeria.show()
    # preparamos método para cuando se cierre la aplicación.
    sys.exit(app.exec_())