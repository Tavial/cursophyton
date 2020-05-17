"""
    Definimos la clase Fecha
"""
from datetime import datetime

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
