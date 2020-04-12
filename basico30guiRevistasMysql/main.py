'''
Módulo principal del Gestor de Revistas

'''
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow,QMessageBox
import sys
from ventanas import ventana_principal, registro_revista, listado_revistas, ventana_list_widget_revistas, ventana_table_widget_revistas, ventana_edicion
from modelo.clases import Revista
from PyQt5 import QtWidgets
from modelo import operaciones_bd, clases
from modelo.operaciones_bd import obtener_revistas
from PyQt5.Qt import QTableWidgetItem, QButtonGroup, QPushButton, QImage, QPixmap, QIcon, QLabel
from _functools import partial



class VentanaPrincipal (QMainWindow): # Creamos la clase Ventana Principal que hereda de QMainWindow)
    def __init__(self): # definimos el método constructor de nuestra clase Ventana Principal
        super ().__init__() # invocamos al constructor de la clase padre QMainWindow
        self.ventana = ventana_principal.Ui_MainWindow () #instanciamos nuevo objeto ventana de la clase Ui_MainWindow que está en ventana_principal del Designer
        # inicializamos la interfaz donde tenemos nuestros componentes: botones, etiquetas, etc...
        self.ventana.setupUi(self)
        # capturamos los eventos del Menú 
        self.ventana.submenu_registrar_revista.triggered.connect(self.mostrar_registro_revista)
        self.ventana.submenu_listar_revistas.triggered.connect(self.mostrar_listado_revistas)  
        self.ventana.submenu_list_widget_revistas.triggered.connect(self.mostrar_list_widget_revistas)
        self.ventana.submenu_table_widget_revistas.triggered.connect(self.mostrar_table_widget_revistas)
    
    def mostrar_registro_revista(self):
        self.registrar = registro_revista.Ui_MainWindow () # instanciamos nuevo objeto registro de la clase Ui_MainWindow que está en registro_revista del Designer
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú registrar Revista
        self.registrar.setupUi(self)
        self.registrar.boton_registrar_revista.clicked.connect(self.registrar_revista)
        
    def mostrar_listado_revistas (self):
        self.listar = listado_revistas.Ui_MainWindow () #instanciamos nuevo objeto listar de la clase Ui_MainWindow que está en listado_revista del Designer
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú listar Revistas
        self.listar.setupUi(self)
        revistas = operaciones_bd.obtener_revistas()
        texto =""
        for r in revistas: 
            texto += str(r[0])+" " +str(r[1])+" "+str(r[2])+" \n"
        self.listar.listado_revistas.setText(texto)
        
        
    def mostrar_list_widget_revistas (self):
        self.list_widget = ventana_list_widget_revistas.Ui_MainWindow()
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú listar Revistas con List Widget
        self.list_widget.setupUi(self)
        revistas = operaciones_bd.obtener_revistas()
        texto =""
        for r in revistas: 
            texto = "Título: "+str(r[1])+" Precio: " +str(r[2])+" Tema: "+str(r[3])
            self.list_widget.list_widget_revistas.addItem(texto)
            
    def mostrar_table_widget_revistas(self):
        self.table_widget = ventana_table_widget_revistas.Ui_MainWindow()
        #inicializamos la interfaz donde tenemos nuestros componentes del submenú listar Revistas con Table Widget
        self.table_widget.setupUi(self)
        lista_revistas = operaciones_bd.obtener_revistas()
        fila = 0
        for revista in lista_revistas:
            columna = 0
            self.table_widget.tableWidget.insertRow(fila) #voy insertando fila
            print (str(revista))
            for registro in revista:
                celda = QTableWidgetItem (str(registro)) 
                print (str(registro))
                self.table_widget.tableWidget.setItem(fila,columna,celda) 
                columna+=1
            
            #creamos los botones borrar y editar
            self.boton_editar = QPushButton ("Editar")
            revista_a_editar = revista[0] # le pasamos el índice de la revista a editar
            self.boton_editar.clicked.connect(partial(self.editar_revista,revista_a_editar))
            
            
            self.boton_borrar = QPushButton ("Borrar")  
            id_revista_a_borrar = revista[0] # le pasamos el índice de la revista a borrar
            self.boton_borrar.clicked.connect(partial(self.borrar_revista,id_revista_a_borrar))
            
                    
            
            #los añadimos a la table_widget
            self.table_widget.tableWidget.setCellWidget(fila,columna,self.boton_editar)
            self.table_widget.tableWidget.setCellWidget(fila,columna+1,self.boton_borrar)
            
            fila +=1 
            
    
    def borrar_revista (self,id_revista_a_borrar):
        decision = QMessageBox.question (self,"Información","vas a borrar la revista"+str(id_revista_a_borrar))
        if decision == QMessageBox.Yes: # si escogemos que si
            operaciones_bd.borrar_revista(id_revista_a_borrar)
            
        self.mostrar_table_widget_revistas()
        
        
    
    def editar_revista (self,id_revista_a_editar):
        QMessageBox.about (self,"Información","vas a editar la revista"+str(id_revista_a_editar))
        self.v_edicion = ventana_edicion.Ui_ventanaEdicion()
        self.v_edicion.setupUi(self)
        self.revista_editar = operaciones_bd.obtener_revista(id_revista_a_editar)
        #Rellenamos los elementos de la pantalla Editar_revista
        self.v_edicion.entrada_titulo.setText(self.revista_editar.titulo)
        self.v_edicion.entrada_tema.setText(self.revista_editar.tema)
        self.v_edicion.entrada_precio.setText(str(self.revista_editar.precio))
        #Programamos el botón para guardar modificaciones
        self.v_edicion.boton_modificar_revista.clicked.connect (partial(self.modificar_revista,self.revista_editar.id))
        
        
        
    def modificar_revista (self,id_revista_a_editar):
        decision = QMessageBox.question (self,"Información","vas a modificar la revista"+str(id_revista_a_editar))
        if decision == QMessageBox.Yes:
            self.revista_modificada = clases.Revista ()
            self.revista_modificada.id = int(id_revista_a_editar)
            self.revista_modificada.titulo = self.v_edicion.entrada_titulo.text()
            self.revista_modificada.precio = float (self.v_edicion.entrada_precio.text())
            self.revista_modificada.tema = self.v_edicion.entrada_tema.text()
            operaciones_bd.modificar_revista(self.revista_modificada)
            self.mostrar_table_widget_revistas()
            
            
    def registrar_revista(self):
        revista = Revista()
        revista.titulo = self.registrar.entrada_titulo.text()
        revista.precio = float (self.registrar.entrada_precio.text())
        revista.tema = self.registrar.entrada_tema.text()
        #falta validarla y dar errores.
        operaciones_bd.registro_revista(revista)
        #limpio los controles
        self.registrar.entrada_titulo.setText("")
        self.registrar.entrada_precio.setText("")
        self.registrar.entrada_tema.setText("")
        
        #indicamos registro ok al usuario
        QMessageBox.about(self,"Información","Revista registrada correctamente")
    
        
        


if __name__ == "__main__":
    # Creo el entorno (instancia de la clase QApplication)
    app = QApplication(sys.argv)
    # Creo una instancia de la clase que hemos creado (objeto ventana)
    ventana = VentanaPrincipal()
    # Muestro la ventana
    ventana.show()
    # evento de salida
    sys.exit(app.exec_())
    
    
    
    
        



