'''
Módulo principal de la aplicación MODELISMO FERROVIARIO

'''
# importamos de QtWidgets todo lo necesario para trabajar con la ventana, para 
# crear la aplicación y para mostrar mensajes de texto
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QTableWidgetItem

# importamos estos componentes para poder poner una imagen de fondo.

import sys
# importamos la clase Producto que la tenemos en el paquete modelo y el archivo 
# clases.py 
from modelo.clases import Producto, Validador
# importamos todos los comandos SQL que vamos a tener en el paquete modelo y el
# archivo constantes_sql.py
from modelo.constantes_sql import *
# importamos las ventanas que van a conformar nuestro proyecto
from ventanas import ventana_principal, ventana_alta, ventana_listados, ventana_listados_lista, ventana_edicion  
from PyQt5.QtGui import QPixmap
from modelo import operaciones_bd, clases
from PyQt5.Qt import QLabel, QPushButton
from _functools import partial




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
        self.v_principal.accion_listar_tabla.triggered.connect(self.tablaProductos)
        self.v_principal.accion_listar_lista.triggered.connect(self.listaProductos)
    
    
    #######################  METODOS PARA REGISTRAR NUEVO PRODUCTO  #####################
    
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
        # Cuando pulsamos el boton registrar producto llama al método que comprueba que los campos son correctos y lo graba en la B.D
        self.v_alta.boton_registrar.clicked.connect(self.registrarProducto)
        # Cuando pulsamos el radio Digital tenemos que activar el check con sonido.
        self.v_alta.radio_digital.clicked.connect(self.elegirTecnologia)
        self.v_alta.radio_analogica.clicked.connect(self.elegirTecnologia)
        
    
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
        validador = clases.Validador() # creamos un objeto de la clase validador
        referencia = str(self.v_alta.line_referencia.text()) # evaluamos que el campo referencia no esté vacío o con espacios en blanco
        expresion_correcta = validador.noVacio(referencia) 
        if not expresion_correcta:
            QMessageBox.about(self,"Faltan campos","El campo referencia está en blanco")
        else: # pasamos a evaluar el campo nombre
            nombre = str(self.v_alta.line_nombre.text())
            expresion_correcta = validador.noVacio (nombre)
            if not expresion_correcta:
                QMessageBox.about(self,"Faltan campos","El campo nombre está en blanco")
            else: # pasamos a evaluar el campo precio
                precio = str(self.v_alta.line_precio.text())
                expresion_correcta = validador.numReal(precio)
                if not expresion_correcta: 
                    QMessageBox.about(self,"Faltan campos","El campo precio o está en blanco o no tiene un formato correcto.")
                else: # pasamos a evaluar el campo stock. Tiene que ser un entero mayor que 0
                    stock = str(self.v_alta.line_stock.text())
                    expresion_correcta = validador.numEntero(stock)
                    if not expresion_correcta: 
                        QMessageBox.about(self,"Faltan campos","El campo stock o está en blanco o no tiene un formato correcto.")
                    else: # pasamos a evaluar el campo descripcion
                        descripcion = str(self.v_alta.edit_descripcion.toPlainText())
                        expresion_correcta = validador.noVacio(descripcion)
                        if not expresion_correcta: 
                            QMessageBox.about(self,"Faltan campos","El campo descripción está en blanco")
        
                        else: # todo correcto  
                            if precio.find(",") != -1: #si ha introducido una coma la transformamos en punto
                                precio = precio.replace (",",".")
                            item = Producto ()
                            item.referencia = referencia
                            item.nombre = nombre
                            item.tipo = str (self.v_alta.combo_tipo.currentText())
                            item.escala = str (self.v_alta.combo_escala.currentText())
                            item.fabricante = str (self.v_alta.combo_fabricante.currentText())
                            item.precio = float (precio)
                            item.stock = int (stock)
                            if self.v_alta.radio_analogica.isChecked():
                                item.tecnologia = str (self.v_alta.radio_analogica.text())
                            elif self.v_alta.radio_digital.isChecked():
                                if self.v_alta.check_digital.isChecked():
                                    item.tecnologia = "Digital "+str (self.v_alta.check_digital.text())
                                else: 
                                    item.tecnologia = str (self.v_alta.radio_digital.text()) 
                            item.descripcion = descripcion
                            item.imagen = self.image
                            # llamamos al método que almacena todos los campos del objeto item en la BB.DD
                            operaciones_bd.registro_producto(item)   
                            
                            
                            QMessageBox.about(self,"OK","Se ha guardado el registro con éxito.")    
                            #limpiamos los campos: 
                            self.v_alta.line_referencia.setText("")
                            self.v_alta.line_nombre.setText("")
                            self.v_alta.line_precio.setText("")
                            self.v_alta.line_stock.setText("")
                            self.v_alta.visor_imagen.setPixmap(QPixmap(""))
                            self.v_alta.edit_descripcion.setText("")
                  
            
    def elegirTecnologia (self):
        if self.v_alta.radio_digital.isChecked(): #si marcamos la casilla de digital, activamos el check con sonido
            self.v_alta.check_digital.setEnabled (True)
        
        if self.v_alta.radio_analogica.isChecked (): # si marcamos la casilla de analógico, desactivamos el check con sonido y lo desmarcamos en caso de que estuviese marcado
            self.v_alta.check_digital.setEnabled (False)
            self.v_alta.check_digital.setChecked(False)
          
    #######################  METODOS PARA LISTAR LOS PRODUCTOS  #####################
    
    ### Con ListWidget
        
    def listaProductos(self): 
        self.v_lista = ventana_listados_lista.Ui_ventanaListadosLista ()
        self.v_lista.setupUi(self)
        self.setStyleSheet("VentanaPrincipal {background-image: none}")
        self.decorarVentanaListadosLista () 
        # Llamamos al método listar producto que nos devuelve una lista con los campos de la tabla_productos de la base de datos bd_model_ferro
        self.lista = operaciones_bd.listar_productos() 
        for elemento in self.lista:
            linea1 = "REF: "+str(elemento[0])+"  "+str(elemento[1])+"\n"
            linea2 = "TIPO: "+str(elemento[2])+"\n"
            linea3 = "ESCALA: "+str(elemento[3])+"\n"
            linea4 = "FABRICANTE: "+str(elemento[4])+"\n"
            linea5 = "PRECIO: "+str(elemento[5])+" €"+"\n"
            linea6 = "TECNOLOGIA: "+str(elemento[7])+"\n"
            linea7 = "DESCRIPCION: "+str(elemento[8])+"\n"
            linea8 = "STOCK: "+str(elemento[6])+"\n\n"
            linea9 = "-----------------------------------------------------------------------------------------------------------\n"
            texto = linea1+linea2+linea3+linea4+linea5+linea6+linea7+linea8+linea9
            self.v_lista.visor_listado.addItem(texto)
            
    ### Con TableWidget
            
    def tablaProductos(self):   
        self.v_tabla = ventana_listados.Ui_ventanaListados()
        self.v_tabla.setupUi(self)   
        self.setStyleSheet("VentanaPrincipal {background-image: none}") 
        self.decorarVentanaListadosTabla ()
        # Llamamos al método listar producto que nos devuelve una lista con los campos de la tabla_productos de la base de datos bd_model_ferro 
        self.lista = operaciones_bd.listar_productos() 
        # Llamamos al método rellenarTabla que rellenerá la Table Widget con los valores extraídos en la consulta
        self.rellenarTabla ()
       
             
    
    def rellenarTabla(self):
        fila = 0
        for registro in self.lista:
            # insertamos cada fila      
            self.v_tabla.tabla.insertRow(fila)
            self.v_tabla.tabla.setRowHeight(fila,80) 
            columna = 0
            for campo in registro: 
                celda = QTableWidgetItem(str(campo))  
                validador = str(campo)
                if validador.find(":/") != -1: # es el campo imagen 
                    ico = QLabel ()
                    pixmap = QPixmap (validador)
                    reducido = pixmap.scaled(100,80)
                    ico.setPixmap(reducido)
                    ico.setContentsMargins (0, 0, 0, 0)
                    self.v_tabla.tabla.setCellWidget(fila,columna,ico)
                else:            
                    self.v_tabla.tabla.setItem (fila,columna,celda)
                columna += 1 
            
            # añadimos las columnas de botones
            
            # VISUALIZAR
            self.v_tabla.tabla.setColumnWidth(columna,32) # el ancho de la columna será más estrecho
            self.boton_ver = QPushButton()
            self.boton_ver.clicked.connect(partial(self.verImagen,validador))  
            self.boton_ver.setStyleSheet("background-image:url('iconos/ver.png'); background-repeat:no-repeat; background-position:center")
            self.v_tabla.tabla.setCellWidget(fila,columna,self.boton_ver)
            
            #EDITAR
            self.v_tabla.tabla.setColumnWidth(columna+1,32) # el ancho de la columna será más estrecho
            self.boton_editar = QPushButton()
            self.boton_editar.clicked.connect(partial(self.editar,registro[0]))  
            self.boton_editar.setStyleSheet("background-image:url('iconos/editar.png'); background-repeat:no-repeat; background-position:center")
            self.v_tabla.tabla.setCellWidget(fila,columna+1,self.boton_editar)
            
            #BORRAR  
            self.v_tabla.tabla.setColumnWidth(columna+2,32) # el ancho de la columna será más estrecho
            self.boton_borrar = QPushButton()
            self.boton_borrar.clicked.connect(partial(self.borrar,registro[0]))  
            self.boton_borrar.setStyleSheet("background-image:url('iconos/borrar.png'); background-repeat:no-repeat; background-position:center")
            self.v_tabla.tabla.setCellWidget(fila,columna+2,self.boton_borrar)
                     
            fila += 1
     
    def verImagen (self,imagen_a_mostrar): # Permite visualizar la imagen del producto cuando se pulsa el icono del ojo
        self.v_tabla.visor_imagen.setPixmap(QPixmap(imagen_a_mostrar))
    
    
    #######################  METODOS PARA EDITAR UN PRODUCTO #####################       
    
    def editar (self,registro):
        self.v_edicion = ventana_edicion.Ui_ventanaEdicion()
        self.v_edicion.setupUi(self)
        self.decorarVentanaEdicion()
        self.producto_a_editar = operaciones_bd.obtener_producto(registro)
        self.v_edicion.line_referencia.setText(self.producto_a_editar.referencia)
        self.v_edicion.line_referencia.setDisabled (True)
        self.v_edicion.line_nombre.setText(self.producto_a_editar.nombre)
        self.v_edicion.combo_tipo.setCurrentText(self.producto_a_editar.tipo) 
        self.v_edicion.combo_escala.setCurrentText(self.producto_a_editar.escala)
        self.v_edicion.combo_fabricante.setCurrentText(self.producto_a_editar.fabricante)
        self.v_edicion.line_precio.setText(str(self.producto_a_editar.precio))
        self.v_edicion.line_stock.setText(str(self.producto_a_editar.stock))
        tech = str(self.producto_a_editar.tecnologia)
        if tech == "Digital":
            self.v_edicion.radio_digital.setChecked(True)
            self.v_edicion.check_digital.setEnabled(True)
        elif tech == "Digital con sonido":
            self.v_edicion.radio_digital.setChecked(True)
            self.v_edicion.check_digital.setChecked(True)
            self.v_edicion.check_digital.setEnabled (True)
        else: #tech == "Analógico"
            self.v_edicion.radio_analogica.setChecked(True)
            self.v_edicion.check_digital.setChecked(False)
            self.v_edicion.check_digital.setEnabled(False)
            
        self.v_edicion.edit_descripcion.setText(self.producto_a_editar.descripcion)
        self.v_edicion.visor_imagen.setPixmap(QPixmap(self.producto_a_editar.imagen))
        self.image = self.producto_a_editar.imagen
        
        
        # Cuando pulsamos el radio Digital tenemos que activar el check con sonido.
        self.v_edicion.radio_digital.clicked.connect(self.elegirTecnologia_editar)
        self.v_edicion.radio_analogica.clicked.connect(self.elegirTecnologia_editar)
        
        # Cuando pulsamos el botón Cargar Imagen llamamos a un método para poder seleccionar la imagen y cargarla
        self.v_edicion.boton_imagen.clicked.connect(self.cargarImagen_editar)
        
        self.v_edicion.boton_modificar.clicked.connect(partial(self.modificarProducto,self.producto_a_editar.referencia))
        
    
    def elegirTecnologia_editar (self):
        if self.v_edicion.radio_digital.isChecked(): #si marcamos la casilla de digital, activamos el check con sonido
            self.v_edicion.check_digital.setEnabled (True)
        
        if self.v_edicion.radio_analogica.isChecked (): # si marcamos la casilla de analógico, desactivamos el check con sonido y lo desmarcamos en caso de que estuviese marcado
            self.v_edicion.check_digital.setEnabled (False)
            self.v_edicion.check_digital.setChecked(False)    
    
    
    def cargarImagen_editar (self):
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
            self.v_edicion.visor_imagen.setPixmap(QPixmap(img))
            self.image = img  
            
    
    def modificarProducto (self,registro_a_cambiar):
        eleccion = QMessageBox.question(self,"Alerta","Vas a modificar el registro con ref: "+str(registro_a_cambiar))
    
        if eleccion == QMessageBox.Yes:
            producto_modificado = clases.Producto()
            producto_modificado.referencia = registro_a_cambiar
            
            validador = clases.Validador() # creamos un objeto de la clase validador
            # pasamos a evaluar el campo nombre
            nombre = str(self.v_edicion.line_nombre.text())
            expresion_correcta = validador.noVacio (nombre)
            if not expresion_correcta:
                QMessageBox.about(self,"Faltan campos","El campo nombre está en blanco")
            else: # pasamos a evaluar el campo precio
                precio = str(self.v_edicion.line_precio.text())
                expresion_correcta = validador.numReal(precio)
                if not expresion_correcta: 
                    QMessageBox.about(self,"Faltan campos","El campo precio o está en blanco o no tiene un formato correcto.")
                else: # pasamos a evaluar el campo stock. Tiene que ser un entero mayor que 0
                    stock = str(self.v_edicion.line_stock.text())
                    expresion_correcta = validador.numEntero(stock)
                    if not expresion_correcta: 
                        QMessageBox.about(self,"Faltan campos","El campo stock o está en blanco o no tiene un formato correcto.")
                    else: # pasamos a evaluar el campo descripcion
                        descripcion = str(self.v_edicion.edit_descripcion.toPlainText())
                        expresion_correcta = validador.noVacio(descripcion)
                        if not expresion_correcta: 
                            QMessageBox.about(self,"Faltan campos","El campo descripción está en blanco")
        
                        else: # todo correcto  
                            if precio.find(",") != -1: #si ha introducido una coma la transformamos en punto
                                precio = precio.replace (",",".")

                            producto_modificado.nombre = self.v_edicion.line_nombre.text()
                            producto_modificado.tipo = self.v_edicion.combo_tipo.currentText()
                            producto_modificado.escala = self.v_edicion.combo_escala.currentText()
                            producto_modificado.fabricante = self.v_edicion.combo_fabricante.currentText()
                            producto_modificado.precio = float(precio)
                            producto_modificado.stock = int(self.v_edicion.line_stock.text())
                            if self.v_edicion.radio_analogica.isChecked():
                                producto_modificado.tecnologia = str (self.v_edicion.radio_analogica.text())
                            elif self.v_edicion.radio_digital.isChecked():
                                if self.v_edicion.check_digital.isChecked():
                                    producto_modificado.tecnologia = "Digital "+str (self.v_edicion.check_digital.text())
                                else: 
                                    producto_modificado.tecnologia = str (self.v_edicion.radio_digital.text()) 
                            producto_modificado.descripcion = self.v_edicion.edit_descripcion.toPlainText()
                            producto_modificado.imagen = self.image
    
                            operaciones_bd.guardar_cambios_producto (producto_modificado)
        
                            self.tablaProductos()    
                            
    
    #######################  METODO PARA BORRAR UN PRODUCTO #####################    
        
    def borrar (self,registro):
        eleccion = QMessageBox.question(self,"Alerta","Vas a borrar el registro con ref: "+str(registro))
        
        if eleccion == QMessageBox.Yes:
            operaciones_bd.borrar_producto(registro)
            
        self.tablaProductos()
                      
    
    ############ METODOS DE ASPECTO DE LAS VENTANAS   ###############################
    
    def decoraPortada (self):
        # ponemos una imagen de fondo de pantalla
        self.setStyleSheet("VentanaPrincipal {background-image: url(imagenes/Fondo.png)}")
        # cambiamos el color del texto de la etiqueta principal
        self.v_principal.etq_titulo.setStyleSheet ("color: white")
        # cambiamos el color de fondo de la barra del menú
        self.v_principal.Menu.setStyleSheet("background-color:white; color:black; font-size:22px")
        # cambiamos el color de fondo de las opciones del menún
        self.v_principal.menuProductos.setStyleSheet("background-color:black; color:white ")
    
    
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
        self.v_alta.caja.setStyleSheet("font-size:16px")
        self.v_alta.edit_descripcion.setStyleSheet("font-size: 16px; background-color:white")
        self.v_alta.boton_imagen.setStyleSheet("background-color:#A4C5C6")
        self.v_alta.boton_registrar.setStyleSheet("background-color:#A4C5C6")
        
    def decorarVentanaEdicion(self):
          
        self.setStyleSheet("background-color:#DFCDC3")
        self.v_edicion.etq_titulo.setStyleSheet("color:black; background-color:#DFCDC3")
        self.v_edicion.line_nombre.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_edicion.line_precio.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_edicion.line_referencia.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_edicion.line_stock.setStyleSheet ("font-size: 16px; background-color:white")
        self.v_edicion.combo_escala.setStyleSheet("background-color:white")
        self.v_edicion.combo_fabricante.setStyleSheet("background-color:white")
        self.v_edicion.combo_tipo.setStyleSheet("background-color:white")
        self.v_edicion.caja.setStyleSheet("font-size:16px")
        self.v_edicion.edit_descripcion.setStyleSheet("font-size: 16px; background-color:white")
        self.v_edicion.boton_imagen.setStyleSheet("background-color:#A4C5C6")
        self.v_edicion.boton_modificar.setStyleSheet("background-color:#A4C5C6")
    
        
    def decorarVentanaListadosTabla(self):
        
        self.setStyleSheet("background-color:#DFCDC3")
        self.v_tabla.tabla.setStyleSheet("color:#204151; font-weight:bold")
        self.v_tabla.etq_principal.setStyleSheet("color:black; background-color:white")
        self.v_tabla.etq_informativa.setStyleSheet("color:#204151")   
        self.v_tabla.visor_imagen.setStyleSheet("background-color:white")  
        
    def decorarVentanaListadosLista(self):
        
        self.setStyleSheet("background-color:#DFCDC3")
        self.v_lista.visor_listado.setStyleSheet("color:#204151; font-size:16px; font-weight:bold")
        self.v_lista.etq_principal.setStyleSheet("color:black; background-color:white")
          
    
    ##########################################################################################
           
if __name__ =="__main__":
       
    # instanciamos un objeto de la clase QApplication
    app = QApplication (sys.argv)
    # instanciamos un objeto de nuestra clase VentanaPrincipal ()
    v_principal = VentanaPrincipal()

    # mostramos la ventana principal
    v_principal.show()
    # preparamos el evento de salida de la aplicación
    sys.exit (app.exec_())
    
        