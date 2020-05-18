class Kaprekar ():
    def __init__(self):
        self.kte_kaprekar = "6174"
        
    def ascendente(self,numero):
        resultado = "".join(sorted(numero))
        return resultado
    
    def descendente(self,numero):
        resultado = "".join(sorted(numero,reverse=True))
        return resultado
    
    def calculoVueltas(self,numero):
        vueltas = 0    
        while numero != self.kte_kaprekar and vueltas <= 7:      
            ascendente = self.ascendente (numero)
            descendente = self.descendente (numero)
            numero = int(descendente) - int(ascendente)
            numero = str(numero)
            if len(numero) < 4:
                for i in range (len(numero),4):
                    numero = "0"+numero
            vueltas += 1 
        return vueltas    
        
        
        
