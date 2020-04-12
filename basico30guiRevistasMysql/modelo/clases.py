
class Revista ():
    def __init__(self,id = 0, titulo = "",precio = 0.0, tema = ""):
        self.titulo = titulo
        self.precio = precio
        self.tema = tema
        self.id = id
        
    def a_texto(self):
        return "titulo: {} precio: {} tema: {}".format(self.titulo,self.precio,self.tema)