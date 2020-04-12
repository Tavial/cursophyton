'''
Definimos las clases de nuestra aplicación MODELISMO FERROVIARIO

'''
class Producto ():
    def __init__(self,referencia = "",nombre = "", tipo="Máquinas",escala = "H0",fabricante = "Marklin",precio = 0.0, stock = 0, descripcion="", imagen=""):
        self.referencia = referencia
        self.nombre = nombre
        self.tipo = tipo
        self.escala = escala
        self.fabricante = fabricante
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.imagen = imagen
