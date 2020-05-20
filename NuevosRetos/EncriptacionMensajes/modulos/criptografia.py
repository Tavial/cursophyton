class Vigenere():
    def __init__(self):
        self.abecedario = ["A","a","Á","á","B","b","C","c","D","d","E","e","É","é","F","f","G","g","H","h",
                           "I","i","Í","í","J","j","K","k","L","l","M","m","N","n","Ñ","ñ","O","o","Ó","ó",
                           "P","p","Q","q","R","r","S","s","T","t","U","u","Ú","ú","Ü","ü","V","v","W","w",
                           "X","x","Y","y","Z","z"]
        self.dimension = 66
        
    def rellenarCuadro(self):
        cuadro = []
        k = 0
        vueltas = 0
        for i in range (self.dimension):
            cuadro.append ([]) 
            for j in range (self.dimension):
                cuadro [i].append(self.abecedario[k])
                k += 1
                if k > 65: 
                    k = 0
            vueltas += 1
            k = vueltas 
        return cuadro
    
    def imprimirCuadro (self,cuadro):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print (cuadro[i][j],end=" ")
            print ()
        print ()
    
    def encriptar (self,cuadro,x,y):
        for i in range (self.dimension):
            if x == cuadro [i][0]:
                posicion_x = i
        for j in range (self.dimension):
            if y == cuadro [posicion_x][j]:
                posicion_y = j
        return cuadro [0][posicion_y]
                
    def desencriptar (self,cuadro,x,y):
        for i in range (self.dimension):
            if x == cuadro [i][0]:
                posicion_x = i
        for j in range (self.dimension):
            if y == cuadro [0][j]:
                posicion_y = j
        return cuadro[posicion_x][posicion_y]
        