class Operaciones():
    
    def __init__(self):
        self.semana = ("MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO")
        
    def mayor(self,lista):
        mayor = -1
        empate = 0 
        indice = 0
        for elemento in range(len(lista)): 
            if float(lista[elemento]) > mayor:
                mayor = lista[elemento]
                indice = elemento
                empate = False
            elif float(lista[elemento])== mayor:    
                empate = True
        if empate == True:
            return "EMPATE"
        else:
            return self.semana[indice]
        
    def menor(self,lista):
        menor = lista[0]
        empate = False
        indice = 0
        for elemento in range(len(lista)): 
            if float(lista[elemento]) <= menor:
                if float(lista[elemento])== menor:  
                    if elemento != 0:  
                        empate = True
                else:
                    menor = lista[elemento]
                    indice = elemento
                    empate = False      
        if empate == True:
            return "EMPATE"
        else:
            return self.semana[indice]
        
    def mediaSemanal (self,lista):
        ganancia_domingo = lista[len(lista)-1]
        suma = 0
        for elemento in range(len(lista)):
            suma += float(lista[elemento])
        media = suma / len(lista)
        if ganancia_domingo > media: 
            return "SI"
        else: 
            return "NO"
        