'''
Antes de ser ese dispositivo de comunicación tan extendido, se entendía por móvil una estructura hecha 
con alambres y cuerdas de las que colgaban figuras coloridas, y que se colocaban sobre las cunas de los 
bebés para estimularles y entretenerles.

La representación de un móvil simple consta de un único alambre colgado de una cuerda, con un objeto a 
cada lado. En realidad se puede ver como una "balanza" con el punto de apoyo en el sitio donde la cuerda 
está unida al alambre. Según el principio de la palanca, sabemos que está en equilibrio si el producto 
del peso de los objetos por sus distancias al punto de apoyo son iguales. Es decir si consideramos pi 
como el peso colgado en el lado izquierdo, pd el peso del lado derecho, y di la distancia desde el peso 
izquierdo a la cuerda y dd de la cuerda al peso derecho, podremos decir que el móvil está en equilibrio 
si se cumple que pi × di = pd × dd.

En móviles más complejos, cada peso puede ser sustituido por un "submóvil". En este caso se considera el 
peso del submóvil como la suma de los pesos de todos sus objetos, despreciando la cuerda y los alambres. 
Y consideraremos que está balanceado si pi × di = pd × dd y, además los submóviles de la izquierda y los 
de la derecha estan a su vez balanceados.

En ese caso no es tan trivial averiguar si está o no balanceado, por lo que te pedimos que nos escribas 
un programa que, dada una descripción de un móvil como entrada, determine si está o no en equilibrio.

Entrada
--------
La entrada está compuesta por una sucesión de casos de prueba, cada una representando un móvil.

Un móvil se describe con una o más líneas, cada una de ellas conteniendo cuatro números enteros positivos, 
separados por un único espacio. Esos cuatro enteros representan las distancias de los extremos al punto 
de apoyo, así como sus pesos, en el orden pi, di, pd, dd.

Si pi o pd (alguno de los pesos) es 0, en el extremo habrá colgado un submóvil, que estará descrito a 
continuación. Si un móvil tiene un submóvil en cada lado, primero se describirá el submóvil izquierdo.

La entrada finalizará con un móvil especial, 0 0 0 0, indicando que no tiene pesos ni distancias y, por 
tanto, no hay móvil.

Salida
Para cada caso de prueba, el programa indicará SI si el móvil que representa está en equilibrio, y NO en 
otro caso. Recuerda que se dice que un móvil está en equilibrio si todos sus submóviles y él mismo lo 
están.

Entrada de ejemplo
------------------
0 2 0 4
0 3 0 1
1 1 1 1
2 4 4 2
1 6 3 2
0 1 3 4
2 3 3 2
0 0 0 0

Salida de ejemplo
-----------------
SI
NO
'''

class Nodo ():
    def __init__(self,dato=None):
        self.info= dato # Dato del nodo del árbol
        self.izq = None # Rama izquierda del árbol
        self.der = None # Rama derecha del árbol
        self.petado = False
        self.equilibrado = False


def insertarSubmovil (arbol,elemento):
    if arbol is None:
        arbol = elemento     
    else:
        if arbol.izq is None:
            if arbol.info[0] == "0": 
                arbol.izq = elemento
            else:
                if arbol.der is None:
                    arbol.der = elemento
            
        else:
            if not arbol.izq.petado:
                insertarSubmovil (arbol.izq,elemento)
            else: 
                if arbol.der is None: 
                    arbol.der = elemento
                else: 
                    if not arbol.der.petado:
                        insertarSubmovil (arbol.der,elemento)

def marcarPetado (arbol):
    if arbol is not None:
        marcarPetado (arbol.izq)
        marcarPetado (arbol.der)
        if arbol.info[0] =="0" and arbol.info[2] == "0":
            if arbol.izq is None or arbol.der is None:
                arbol.petado = False
            elif arbol.izq is not None and arbol.der is not None: 
                if arbol.izq.petado and arbol.der.petado:
                    arbol.petado = True
                else:
                    arbol.petado = False             
        elif arbol.info [0] == "0" and arbol.info[2] != "0":
            if arbol.izq is None:
                arbol.petado = False
            else: 
                arbol.petado = True
        elif arbol.info[0] != "0" and arbol.info[2] == "0":
            if arbol.der is None:
                arbol.petado = False
            else: 
                arbol.petado = True
        elif arbol.info[0] != "0" and arbol.info[2] != "0":
            arbol.petado = True

            
def marcarEquilibrado (arbol):
    if arbol is not None:
        marcarEquilibrado (arbol.izq)
        marcarEquilibrado (arbol.der)
        if arbol.info[0] !="0" and arbol.info[2] != "0": #nodo final
            if int(arbol.info[0])*int(arbol.info[1]) == int(arbol.info[2])*int(arbol.info[3]):
                arbol.equilibrado = True
        elif arbol.info[0] == "0" and arbol.info[2] =="0": # tiene dos hijos
            if arbol.der.equilibrado and arbol.izq.equilibrado:
                arbol.equilibrado = True
                 
            
def movilEquilibrado (arbol): 
    if arbol is not None: 
        if arbol.equilibrado:
            equilibrado = True
        else: 
            equilibrado = False
    return equilibrado
    
def movilLleno (arbol):  
    if arbol is not None: 
        if arbol.petado:
            lleno = True
        else: 
            lleno = False
    return lleno
        
    
    

def recorrerMovil (arbol):
    if arbol is not None:
        print (arbol.info)
        recorrerMovil (arbol.izq)
        recorrerMovil (arbol.der)
        
def borrarMovil (arbol):
    if arbol is not None:
        borrarMovil (arbol.izq)
        borrarMovil (arbol.der)
        if arbol.izq is None and arbol.der is None: 
            del arbol
        
        
#### programa principal  ########################
        
archivo_entrada = open ("entrada.txt","r")
raiz = str(archivo_entrada.readline ()).split()
arbol = Nodo(raiz)
marcarPetado(arbol)
for linea in archivo_entrada:
    if linea != "0 0 0 0\n": # fin de archivo
        nodo = str(linea).split()
        elemento = Nodo(nodo)
        marcarPetado(arbol)
        lleno = movilLleno(arbol)        
        if not lleno:
            insertarSubmovil(arbol,elemento)
        else:
            # Tratamos este móvil
            marcarEquilibrado(arbol)
            equilibrado = movilEquilibrado (arbol)
            recorrerMovil(arbol) 
            if equilibrado: 
                print ("Móvil equilibrado")
            else: 
                print ("Móvil no equilibrado")
            # Borramos el antiguo móvil
            borrarMovil (arbol)
            print ("Móvil borrado")
            print ("")
            print (" -------------------------")
            print ("")
            # empezamos un nuevo móvil
            print ("Móvil nuevo")
            arbol = Nodo(nodo)
    else:
        recorrerMovil(arbol) 
        marcarEquilibrado(arbol)
        equilibrado = movilEquilibrado (arbol)
        if equilibrado: 
            print ("Móvil equilibrado")
        else: 
            print ("Móvil no equilibrado") 
        # Borramos el antiguo móvil
        borrarMovil (arbol)
        print ("Móvil borrado")
          
archivo_entrada.close()
