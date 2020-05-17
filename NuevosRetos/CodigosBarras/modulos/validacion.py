class Codigo ():
    def __init__(self):
        self.ok = False
        self.tipo = None
        self.control = None
        self.longitud = None
        self.diccionario = {"00":"Estados Unidos & Canadá",
                            "01":"Estados Unidos & Canadá",
                            "02":"Estados Unidos & Canadá",
                            "03":"Estados Unidos & Canadá",
                            "04":"Estados Unidos & Canadá",
                            "05":"Estados Unidos & Canadá",
                            "06":"Estados Unidos & Canadá",
                            "07":"Estados Unidos & Canadá",
                            "08":"Estados Unidos & Canadá",
                            "09":"Estados Unidos & Canadá",
                            "10":"Estados Unidos & Canadá",
                            "11":"Estados Unidos & Canadá",
                            "12":"Estados Unidos & Canadá",
                            "13":"Estados Unidos & Canadá",
                            "20":"Reservado para tiendas y supermercados",
                            "21":"Reservado para tiendas y supermercados",
                            "22":"Reservado para tiendas y supermercados",
                            "23":"Reservado para tiendas y supermercados",
                            "24":"Reservado para tiendas y supermercados",
                            "25":"Reservado para tiendas y supermercados",
                            "26":"Reservado para tiendas y supermercados",
                            "27":"Reservado para tiendas y supermercados",
                            "28":"Reservado para tiendas y supermercados",
                            "29":"Reservado para tiendas y supermercados",
                            "30":"Francia & Mónaco",
                            "31":"Francia & Mónaco",
                            "32":"Francia & Mónaco",
                            "33":"Francia & Mónaco",
                            "34":"Francia & Mónaco",
                            "35":"Francia & Mónaco",
                            "36":"Francia & Mónaco",
                            "37":"Francia & Mónaco",
                            "380":"Bulgaria",
                            "383":"Eslovenia",
                            "385":"Croacia",
                            "387":"Bosnia-Herzegovina",
                            "40":"Alemania",
                            "41":"Alemania",
                            "42":"Alemania",
                            "43":"Alemania",
                            "44":"Alemania",
                            "45":"Japón",
                            "46":"Federación Rusa",
                            "471":"Taiwán",
                            "474":"Estonia",
                            "475":"Letonia",
                            "476":"Azerbaiyán",
                            "477":"Lituania",
                            "478":"Uzbekistán",
                            "479":"Sri Lanka",
                            "480":"Filipinas",
                            "481":"Bielorrusia",
                            "482":"Ucrania",
                            "484":"Moldavia",
                            "485":"Armenia",
                            "486":"Georgia",
                            "487":"Kazajstán",
                            "489":"Hong Kong",
                            "49":"Japón",
                            "50":"Gran Bretaña",
                            "520":"Grecia",
                            "528":"Líbano",
                            "529":"Chipre",
                            "531":"Macedonia",
                            "535":"Malta",
                            "539":"Irlanda",
                            "54":"Bélgica & Luxemburgo",
                            "560":"Portugal",
                            "569":"Islandia",
                            "57":"Dinamarca",
                            "590":"Polonia",
                            "594":"Rumanía",
                            "599":"Hungría",
                            "600":"Sudáfrica",
                            "601":"Sudáfrica",
                            "609":"Mauricio",
                            "611":"Marruecos",
                            "613":"Argelia",
                            "619":"Túnez",
                            "621":"Siria", 
                            "622":"Egipto",
                            "624":"Libia",
                            "625":"Jordania",
                            "626":"Irán",
                            "627":"Kuwait",
                            "628":"Arabia Saudita",
                            "629":"Emiratos Árabes Unidos",
                            "64":"Finlandia",
                            "690":"China",
                            "691":"China",
                            "692":"China",
                            "70":"Noruega",
                            "729":"Israel",
                            "73":"Suecia",
                            "740":"Guatemala",
                            "741":"El Salvador",
                            "742":"Honduras",
                            "743":"Nicaragua",
                            "744":"Costa Rica",
                            "745":"Panamá",
                            "746":"República Dominicana",
                            "750":"México",
                            "759":"Venezuela",
                            "76":"Suiza",
                            "770":"Colombia",
                            "773":"Uruguay",
                            "775":"Perú",
                            "777":"Bolivia",
                            "779":"Argentina",
                            "780":"Chile",
                            "784":"Paraguay",
                            "785":"Perú",
                            "786":"Ecuador",
                            "789":"Brasil",
                            "80":"Italia",
                            "81":"Italia",
                            "82":"Italia",
                            "83":"Italia",
                            "84":"España",
                            "850":"Cuba",
                            "858":"Eslovaquia",
                            "859":"República Checa",
                            "860":"Serbia & Montenegro",
                            "869":"Turquía",
                            "87":"Holanda",
                            "880":"Corea del Sur",
                            "885":"Tailandia",
                            "888":"Singapur",
                            "890":"India",
                            "893":"Vietnam",
                            "899":"Indonesia",
                            "90":"Austria",
                            "91":"Austria",
                            "93":"Australia",
                            "94":"Nueva Zelanda",
                            "955":"Malasia",
                            "958":"Macao",
                            "977":"ISSN Para periódicos",
                            "978":"ISBN Para libros",
                            "979":"ISMN Para música"
                            }

    def validarCodigoBarras (self,codigo):
        if len(codigo) > 0 and len(codigo) <= 8:
            self.ok = True
        elif len(codigo) > 8 and len(codigo) <= 13:
            self.ok = True
        else:
            self.ok = False
        return self.ok

    def tipoCodigo (self,codigo):
        if len(codigo) > 0 and len(codigo) <= 8:
            if codigo == "0":
                self.tipo = "salir"
            else:
                self.tipo = "EAN-8"
        elif len(codigo) > 8 and len(codigo) <= 13:
            self.tipo = "EAN-13"

        return self.tipo

    def rellenarConEspacios (self,codigo):
        if len(codigo) > 0 and len(codigo) <= 8:
            if codigo != "0":
                for i in range (len(codigo),8):
                    codigo = "0"+codigo
        elif len(codigo) > 8 and len(codigo) <= 13:
            for i in range (len(codigo),13):
                codigo = "0"+codigo
        return codigo

    def comprobarDigitoControl (self,codigo):
        self.longitud = len(codigo)
        #Vamos a invertir la cadena
        codigo_invertido = codigo[::-1]
        # ahora vamos a eliminar el primer elemento de la cadena ya que es el dígito de control. Antes de quitarlo lo guardamos
        self.control = int (codigo_invertido[0])
        codigo_invertido = codigo_invertido [1:]
        suma = 0
        for i in range (0,self.longitud-1):
            if i % 2:
                suma = suma + (int(codigo_invertido[i])*1)
            else:
                suma = suma + (int(codigo_invertido[i]) * 3)
        acum = 0
        numero = suma
        while numero % 10 != 0:
            acum = acum + 1
            numero = numero +1
        if acum != self.control:
            return False
        else:
            return True    

    def comprobarPais (self,codigo):
        dos_digitos = codigo[0:2]
        tres_digitos = codigo[0:3]
        pais = "Desconocido"
        for cod in self.diccionario.keys():
            if dos_digitos == cod:
                pais = self.diccionario[cod]
            elif tres_digitos == cod:
                pais = self.diccionario[cod]
        return pais    
                

