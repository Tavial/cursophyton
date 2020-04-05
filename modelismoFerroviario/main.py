'''
Módulo principal de la aplicación MODELISMO FERROVIARIO

'''
# importamos de QtWidgets todo lo necesario para trabajar con la ventana, para 
# crear la aplicación y para mostrar mensajes de texto
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QTableWidgetItem, QAbstractItemView

# importamos estos componentes para poder poner una imagen de fondo.

import sys
# importamos la clase Producto que la tenemos en el paquete modelo y el archivo 
# clases.py 
from modelo.clases import Producto
# importamos todos los comandos SQL que vamos a tener en el paquete modelo y el
# archivo constantes_sql.py
from modelo.constantes_sql import *
# importamos las ventanas que van a conformar nuestro proyecto
from ventanas import ventana_principal, ventana_alta, ventana_listados  
from PyQt5.QtGui import QIcon, QPixmap
from modelo import operaciones_bd



class VentanaPrincipal(QMainWindow): # implementamos la clase VentanaPrincipal que
                                    # va a heredar de QMain Window
    
    image = ""
    
    def __init__(self): # implementamos el método constructor de nuestra clase
        super().__init__() # invocamos al método constructor de la clase padre (QMainWindows)
        # a continuación instanciamos un objeto de la clase Ui_ventanaPrincipal
        # creada con el Qt Designer
        self.v_principal = ventana_principal.Ui_ventanaPrincipal ()
        # inicializamos el entorno de las componentes gráficas (labels, menús)
        self.v_principal.setupUi(self)
        
        # Este método proporciona una imagen de fondo a la pantalla principal y cambia colores y tipos de letras    
        self.decoraPortada()
        
        # Aquí capturamos y tratamos los eventos
        self.v_principal.submenu_nuevo_producto.triggered.connect(self.nuevoProducto)
        self.v_principal.submenu_listar_productos.triggered.connect(self.listarProductos)
    
    def decoraPortada (self):
        # ponemos una imagen de fondo de pantalla
        self.setStyleSheet("VentanaPrincipal {background-image: url(imagenes/Fondo.png)}")
        # cambiamos el color del texto de la etiqueta principal
        self.v_principal.etq_titulo.setStyleSheet ("color: white")
        # cambiamos el color de fondo de la barra del menú
        self.v_principal.Menu.setStyleSheet("background-color:white; color:black")
        # cambiamos el color de fondo de las opciones del menún
        self.v_principal.menuProductos.setStyleSheet("background-color:black; color:white ")
    
    def nuevoProducto(self):
        # instanciamos un objeto de la clase Ui_ventanaRegistro creada con el QtDesigner
        self.v_alta = ventana_alta.Ui_ventanaRegistro()
        #inicializamos el entorno de las componentes gráficas (labels, edits, combos, botones, etc)
        self.v_alta.setupUi(self)
        # Quitamos el fondo de pantalla del tren que teníamos como carátula de presentación.
        self.setStyleSheet("VentanaPrincipal {background-image: none}")
        # Este método cambia el aspecto de algunos de los Widgets de la ventana de registro de nuevo producto
        self.decorarVentanaAlta()
        # Cuando pulsamos el botón Cargar Imagen llamamos a un método para poder seleccionar la imagen y cargarla
        self.v_alta.boton_imagen.clicked.connect(self.cargarImagen)
        # Cunado pulsamos el boton registrar producto llama al método que comprueba que los campos son correctos y lo graba en la B.D
        self.v_alta.boton_registrar.clicked.connect(self.registrarProducto)
        
    def cargarImagen (self): 
        dialogo = QFileDialog () #instanciamos un objeto diálogo de la clase QFileDialog
        archivo = dialogo.getOpenFileName(self,'Escoger archivo','D:\\USUARIOS\\TAVIAL\\DOCUMENTOS\\Python\\Ejercicios\\modelismoFerroviario\\imagenes','Imagen Files (*.png *.jpg *.jpeg *.gif *.bmp)')
        if archivo [0]:
            # en la variable archivo se recoge separado por una coma la ruta y el tipo de las imágenes. Lo convertimos a string
            img = str(archivo)
            # este string hacemos con él una lista de dos elementos (el separador es la coma)
            img = img.split(",")
            # cogemos el primer elemento de la lista (índice 0) ya que contiene la ruta que es lo que nos interesa 
            img = str(img[0])
            # quitamos el ( y la ' simple del inicio de la cadena, y la ' final. Nos quedamos con el resto de la cadena
            img = img [2:-1]
            self.v_alta.visor_imagen.setPixmap(QPixmap(img))
            self.image = img
        
            
    
    def registrarProducto(self):    
        referencia = str(self.v_alta.line_referencia.text())
        nombre = str(self.v_alta.line_nombre.text())
        precio = str(self.v_alta.line_precio.text())
        stock = str(self.v_alta.line_stock.text())
        descripcion = str(self.v_alta.edit_descripcion.toPlainText())
        info = QMessageBox()
        if referencia =="" or referencia.isspace(): # el campo referencia no tiene valor  
            info.setWindowTitle ("Faltan campos")
            info.setText("El campo referencia está en blanco")
            x = info.exec_()
        elif nombre =="" or nombre.isspace(): # el campo referencia no tiene valor
            info.setWindowTitle ("Faltan campos")
            info.setText("El campo nombre está en blanco")
            x = info.exec_()
        elif precio =="" or precio.isspace() or precio.isalpha() or precio.find(",") != -1: 
            # el campo precio o está en blanco o está separado por comas en vez de puntos
            info.setWindowTitle ("Faltan campos")
            info.setText("El campo precio o está en blanco o no tiene un formato correcto. El decimal se representa por .")
            x = info.exec_()   
        elif stock =="" or stock.isspace() or stock.isalpha() or stock.find(".") != -1 or stock.find(",") != -1:
            # el campo stock o está en blanco o está separado por comas y puntos por lo que no es un valor entero
            info.setWindowTitle ("Faltan campos")
            info.setText("El campo stock o está en blanco o no tiene un formato correcto. Tiene que ser un entero")
            x = info.exec_() 
        elif descripcion=="" or descripcion.isspace(): # el campo descripción no tiene valor   
            info.setWindowTitle ("Faltan campos")
            info.setText("El campo stock o está en blanco o no tiene un formato correcto. Tiene que ser un entero")
            x = info.exec_() 
        else: #Está todo correcto. Almacenamos los campos en el objeto item que vamos a crear
            item = Producto ()
            item.referencia = referencia
            item.nombre = nombre
            item.tipo = str (self.v_alta.combo_tipo.currentText())
            item.escala = str (self.v_alta.combo_escala.currentText())
            item.fabricante = str (self.v_alta.combo_fabricante.currentText())
            item.precio = float (precio)
            item.stock = int (stock)
            item.descripcion = descripcion
            item.imagen = self.image
            # llamamos al método que almacena todos los campos del objeto item en la BB.DD
            operaciones_bd.registro_producto(item)
        
            info.setWindowTitle ("OK")
            info.setText("Se ha guardado el registro con éxito.")
            x = info.exec_() 
            
            #limpiamos los campos: 
            self.v_alta.line_referencia.setText("")
            self.v_alta.line_nombre.setText("")
            self.v_alta.line_precio.setText("")
            self.v_alta.line_stock.setText("")
            self.v_alta.visor_imagen.setPixmap(QPixmap(""))
            self.v_alta.edit_descripcion.setText("")
            
    def decorarVentanaAlta(self):
        
        self.setStyleSheet("background-color:#DFCDC3")
        self.v_alta.etq_titulo.setStyleSheet("color:black; background-color:#DFCDC3")
        self.v_alta.line_nombre.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_alta.line_precio.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_alta.line_referencia.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_alta.line_stock.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_alta.combo_escala.setStyleSheet("background-color:white")
        self.v_alta.combo_fabricante.setStyleSheet("background-color:white")
        self.v_alta.combo_tipo.setStyleSheet("background-color:white")
        self.v_alta.edit_descripcion.setStyleSheet("font-size: 16px; background-color:white")
        self.v_alta.boton_imagen.setStyleSheet("background-color:#A4C5C6")
        self.v_alta.boton_registrar.setStyleSheet("background-color:#A4C5C6")
        
     
            
    def listarProductos(self):   
        self.v_listados = ventana_listados.Ui_ventanaListados()
        self.v_listados.setupUi(self)    
        self.setStyleSheet("VentanaPrincipal {background-image: none}") 
        self.decorarVentanaListados ()
        # Llamamos al método listar producto que nos devuelve una lista con los campos de la tabla
        self.lista = operaciones_bd.listar_productos() 
        # Llamamos al método rellenarTabla que rellenerá la Table Widget con los valores extraídos en la consulta
        self.rellenarTabla ()
        # Controlamos la pulsación sobre las celdas de la tabla. Si se hacen sobre las que su contenido es una URL de 
        # la imagen del producto, esta se cargará en el campo QLabel que hemos dispuesto para visualizar las imágenes
        self.v_listados.tabla.cellClicked.connect (self.seleccionarCelda)
        
                
    
    def rellenarTabla(self):
        fila = 0
        for registro in self.lista:
            # insertamos cada fila
            self.v_listados.tabla.insertRow(fila)
            columna = 0
            for campo in registro: 
                celda = QTableWidgetItem(str(campo))              
                self.v_listados.tabla.setItem  (fila,columna,celda)
                columna += 1
            fila += 1
     
    def seleccionarCelda(self):     
        
        item = self.v_listados.tabla.currentItem().text()
        icono = str(item)
        self.v_listados.visor_imagen.setPixmap(QPixmap(icono))

        
    def decorarVentanaListados(self):
        
        self.setStyleSheet("background-color:#DFCDC3")
        self.v_listados.tabla.setStyleSheet("color:#204151; font-weight:bold")
        self.v_listados.etq_principal.setStyleSheet("color:black; background-color:white")
        self.v_listados.etq_informativa.setStyleSheet("color:#204151")   
        self.v_listados.visor_imagen.setStyleSheet("background-color:white")      
           
if __name__ =="__main__":
       
    # instanciamos un objeto de la clase QApplication
    app = QApplication (sys.argv)
    # instanciamos un objeto de nuestra clase VentanaPrincipal ()
    v_principal = VentanaPrincipal()

    # mostramos la ventana principal
    v_principal.show()
    # preparamos el evento de salida de la aplicación
    sys.exit (app.exec_())
    
        