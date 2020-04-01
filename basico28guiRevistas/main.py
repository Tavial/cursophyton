'''
Módulo principal del Gestor de Revistas

'''
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
import sys
from ventanas import ventana_principal, registro_revista, listado_revistas 
from PyQt5 import QtWidgets


class VentanaPrincipal (QMainWindow): # Creamos la clase Ventana Principal que hereda de QMainWindow)
    def __init__(self): # definimos el método constructor de nuestra clase Ventana Principal
        super ().__init__() # invocamos al constructor de la clase padre QMainWindow
        self.ventana = ventana_principal.Ui_MainWindow () #instanciamos nuevo objeto ventana de la clase Ui_MainWindow que está en ventana_principal del Designer
        # inicializamos la interfaz donde tenemos nuestros componentes: botones, etiquetas, etc...
        self.ventana.setupUi(self)
        # capturamos los eventos del Menú 
        self.ventana.submenu_registrar_revista.triggered.connect(self.registrarRevista)
        self.ventana.submenu_listar_revistas.triggered.connect(self.listarRevistas)  
        #mostramos la ventana
        self.show()
    
    def registrarRevista(self):
        self.registrar = registro_revista.Ui_MainWindow () # instanciamos nuevo objeto registro de la clase Ui_MainWindow que está en registro_revista del Designer
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú registrar Revista
        self.registrar.setupUi(self)
        #mostramos la ventana
        self.show()
        
    def listarRevistas (self):
        self.listar = listado_revistas.Ui_MainWindow () #instanciamos nuevo objeto listar de la clase Ui_MainWindow que está en listado_revista del Designer
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú listar Revistas
        self.listar.setupUi(self)
        #mostramos la ventana
        self.show()
        


if __name__ == "__main__":
    # Creo el entorno (instancia de la clase QApplication)
    app = QApplication(sys.argv)
    # Creo una instancia de la clase que hemos creado (objeto ventana)
    ventana = VentanaPrincipal()
    # Muestro la ventana
    ventana.show()
    # evento de salida
    sys.exit(app.exec_())
    
    
    
    
        



