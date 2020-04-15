'''
Definimos las clases de nuestra aplicación MODELISMO FERROVIARIO

'''
import re


class Producto ():
    def __init__(self,referencia = "",nombre = "", tipo="Máquinas",escala = "H0",fabricante = "Marklin",precio = 0.0, stock = 0, tecnologia = "Analógica", descripcion="", imagen=""):
        self.referencia = referencia
        self.nombre = nombre
        self.tipo = tipo
        self.escala = escala
        self.fabricante = fabricante
        self.precio = precio
        self.stock = stock
        self.tecnologia = tecnologia
        self.descripcion = descripcion
        self.imagen = imagen
        
class Validador ():
    def __init__(self):
        self.patron_no_vacio = "(^$)|(\s+$)" # que no esté vacío o haya espacios en blanco
        self.patron_num_real = "^\d+((\.|,)\d+)?$"
        self.patron_num_entero = "^[0-9]+$"
        
    def noVacio (self,texto_a_validar):
        valida = re.compile (self.patron_no_vacio)
        resultado_validacion = valida.match (texto_a_validar)
            
        if resultado_validacion:
            return False 
        else: 
            return True
        
    def numReal (self,texto_a_validar):
        valida = re.compile (self.patron_num_real)
        resultado_validacion = valida.match (texto_a_validar)
            
        if resultado_validacion:
            return True 
        else: 
            return False
        
    def numEntero (self,texto_a_validar):
        valida = re.compile (self.patron_num_entero)
        resultado_validacion = valida.match (texto_a_validar)
            
        if resultado_validacion:
            return True 
        else: 
            return False
            
            
        
            
        