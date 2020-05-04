from datetime import datetime
import re

"""
    Definimos la clase anuncio
"""
class Anuncio ():
    def __init__(self,fecha="",escala="1",tipo="1",titulo="",descripcion="",precio=0.0,nomyapell="",email="", emailOK="NO", codigo="", foto=""):
        self.fecha = fecha
        self.escala = escala
        self.tipo = tipo
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio = precio
        self.nomyapell = nomyapell
        self.email = email
        self.emailOK = emailOK
        self.codigo = codigo
        self.foto = foto

"""
    Definimos la clase Fecha
"""

class Fecha ():
    def __init__(self,anyo="", mes="",dia="",hora="",minuto="",fecha=""):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.minuto = minuto
        self.fecha = fecha

    def mostrarFecha (self):
        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        self.fecha = datetime.now()
        #hay un metodo de datetime llamado strftime pero convierte los meses a su nombre inglés
        self.anyo = str(self.fecha.year)
        self.mes = str(self.fecha.month)
        self.dia = str(self.fecha.day)
        hora = self.fecha.hour
        hora = str(hora)
        if len(hora)==1:
            self.hora = "0"+str(hora)
        else:
            self.hora = str(hora)
        self.minuto = str(self.fecha.minute)
        minuto = self.fecha.minute
        minuto =str(minuto)
        if len(minuto) == 1:
            self.minuto = "0" + str(minuto)
        else:
            self.minuto = str(minuto)
        if self.mes =="1":
            self.mes = meses[0]
        elif self.mes =="2":
            self.mes = meses[1]
        elif self.mes =="3":
            self.mes = meses[2]
        elif self.mes =="4":
            self.mes = meses[3]
        elif self.mes =="5":
            self.mes = meses[4]
        elif self.mes =="6":
            self.mes = meses[5]
        elif self.mes =="7":
            self.mes = meses[6]
        elif self.mes =="8":
            self.mes = meses[7]
        elif self.mes =="9":
            self.mes = meses[8]
        elif self.mes =="10":
            self.mes = meses[9]
        elif self.mes =="11":
            self.mes = meses[10]
        elif self.mes =="12":
            self.mes = meses[11]
        fecha = self.dia+" "+self.mes+" "+self.anyo+" - "+self.hora+":"+self.minuto
        return fecha

"""
    Definimos la clase validador
"""

class Validador():
    def __init__(self):
        self.patron_no_vacio = "(^$)|(\s+$)"  # que no esté vacío o haya espacios en blanco
        self.patron_num_real = "^\d+((\.)\d+)?$"
        self.patron_num_entero = "^[0-9]+$"
        self.patron_nombre = "^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$"
        self.patron_email ="^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$"

    def noVacio(self, texto_a_validar):
        valida = re.compile(self.patron_no_vacio)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return False
        else:
            return True

    def numReal(self, texto_a_validar):
        valida = re.compile(self.patron_num_real)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def numEntero(self, texto_a_validar):
        valida = re.compile(self.patron_num_entero)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def nombreApellidos (self, texto_a_validar):
        valida = re.compile(self.patron_nombre)
        resultado_validacion = valida.match(texto_a_validar)

        if resultado_validacion:
            return True
        else:
            return False

    def email (self, texto_a_validar):
        valida = re.compile(self.patron_email)
        resultado_validacion = valida.match(texto_a_validar)
        if resultado_validacion:
            return True
        else:
            return False


