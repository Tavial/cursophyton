'''
Este módulo trabajará con matrices
'''
class Matrices ():
    def crearMatriz (self,dato,dim):
        cadena = dato.split()
        k = 0
        matriz = []
        for i in range (int(dim)):
            matriz.append([])
            for j in range (int(dim)):
                matriz [i].append(cadena[k])
                k += 1
        return matriz
    
    def imprimirMatriz (self,matriz,dim,archivo_salida):
        for i in range(int(dim)):
            for j in range(int(dim)):
                archivo_salida.write (matriz[i][j]+" ")
            archivo_salida.write("\n")
        archivo_salida.write("\n")
    
    def esMagicoDiabolico (self,matriz,dim):
        #sumamos las filas
        constante_magica = 0
        suma = 0
        magico = True
        for i in range (int(dim)):
            for j in range (int(dim)):
                suma = suma + int(matriz[i][j])
            if constante_magica == 0:
                constante_magica = suma
            else:
                if constante_magica != suma: 
                    magico = False
            suma = 0    
        if magico:
            #sumamos las columnas
            constante_magica = 0
            suma = 0
            for j in range (int(dim)):
                for i in range (int(dim)):
                    suma = suma + int(matriz[i][j])
                if constante_magica == 0:
                    constante_magica = suma
                else:
                    if constante_magica != suma: 
                        magico = False
                suma = 0  
        if magico:     
            #sumamos la diagonal principal
            suma_diagonal = 0
            for i in range (int(dim)):
                for j in range (int(dim)):
                    if i == j :
                        suma_diagonal = suma_diagonal + int(matriz[i][j])
        
            if suma_diagonal != constante_magica:
                magico = False
        diccionario = {"magico":magico, "constante_magica":constante_magica}              
        return diccionario
    
    def serie1an2(self,matriz,dim):
        numero = 1
        encontrado = False
        salir = False
        while numero <= int(dim)*int(dim) and not salir:
            for i in range (int(dim)):
                for j in range (int(dim)):
                    if matriz[i][j] == str(numero):
                        encontrado = True    
            if not encontrado:
                salir = True  
            else:      
                numero += 1
                encontrado = False
        if salir == False: 
            return True
        else: 
            return False 
                
    def comprobarEsquinas(self,matriz,dim,cm):
        comprobacion = False
        cm2 = (4 * int(cm)) // int(dim)
    
        suma = int(matriz[0][0]) + int(matriz[0][int(dim)-1]) + int(matriz[int(dim)-1][0]) + int(matriz[int(dim)-1][int(dim)-1])
        if cm2 == suma:
            comprobacion = True
        
        diccionario = {"cm2":cm2, "comprobacion":comprobacion}
    
        return diccionario
    
    def esEsoterico (self,matriz,dim,cte_magica2):  
        esoterico = False
        if int(dim) % 2 != 0:  #si la dimensión es impar
            medio = (int(dim) // 2)
            suma = int(matriz[0][medio]) + int(matriz[medio][0]) + int(matriz [medio][int(dim)-1]) + int(matriz[int(dim)-1][medio])
            if suma == int(cte_magica2):
                casilla_central = int(matriz[medio][medio])*4
                if casilla_central == int (cte_magica2):
                    esoterico = True
        else: # si la dimension es par
            medio = int(dim) // 2
            suma = int(matriz[0][medio-1]) + int(matriz[0][medio]) + int(matriz[medio-1][0]) + int(matriz[medio][0]) + int(matriz[medio-1][int(dim)-1]) + int(matriz[medio][int(dim)-1]) + int(matriz[int(dim)-1][medio-1]) + int(matriz[int(dim)-1][medio]) 
            if suma == 2 * int(cte_magica2):
                casillas_centrales = int(matriz[medio-1][medio-1]) + int(matriz[medio-1][medio]) + int(matriz[medio][medio-1]) + int(matriz[medio][medio])
                if casillas_centrales == int(cte_magica2):
                    esoterico = True
        return esoterico     
            
        