'''
Reino de Dragones
------------------
Nos encontramos en una tierra llena de dragones. Los dragones viven en sus cuevas 
y en ellas guardan sus tesoros. Algunos dragones son buenos y compartirán su 
tesoro, otros dragones son codiciosos y hambrientos y se comerán a cualquiera 
que pise su cueva. El jugador se encuentra frente a las dos cuevas, una con un 
dragón amable y otra con un dragón hambriento. El jugador tiene que elegir a 
cual cueva entrar, sin saber de antemano donde esta uno u el otro.

Mientras el jugador vaya ganando, ira acumulando puntos.
Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le 
acreditan 100 puntos, entra en la segunda cueva y gana el tesoro, se le 
acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el total 
de los puntos que realizo y la opción de empezar de nuevo.
 

'''
#####################  LIBRERIAS IMPORTADAS
import random # para el aleatorio
import time # para el tiempo

puntuacion = 0


def introduccion(): 
    print ("¿¿¿ Qué hago yo aquí ???")
    print("")
    print ("")
    time.sleep(3)
    print ("Me he despertado en las caballerizas de una aldea medieval. ")
    time.sleep(2)
    print ("Me miro...y ...")
    print("")
    time.sleep(3)
    print ("¡¡voy vestida con una brillante armadura!!")
    time.sleep(2)
    print ("")
    print ("A mi lado tengo un precioso corcel negro lujosamente engalanado.")
    time.sleep(2)
    print ("")
    print ("No sé que hago aquí...y me duele algo la cabeza.")
    time.sleep(3)
    print ("")
    print ("Veo que en mi mano hay un cilindro que guarda un pergamino.")
    time.sleep(2)
    print ("")
    print ("Lo abro, lo extiendo y aparece ante mis ojos un mapa de la zona. Empiezo a leer...")
    time.sleep (3)
    print ("")
    print (" 'REINO DE DRAGONES - En el gran bosque cercano los dragones viven en")
    print (" sus cuevas y en ellas guardan sus tesoros. Algunos dragones son ")
    print (" buenos y compartirán su tesoro, otros dragones son codiciosos y ")
    print (" hambrientos y se comerán a cualquiera que pise su cueva. '")
    time.sleep (6)
    print ("")
    print ("")
    print ("Mi ambición me puede ¡¡y me embarco en la aventura!!")
 
def seguirJugando():
    print ("")
    print ("¿quieres seguir jugando? (s/n): ")
    seguir = input()
    seguir = seguir.lower()
    while seguir == "" or seguir.isspace() or seguir.isdigit() or ((seguir != "s") and (seguir != "n")): 
        print ("El valor introducido no es correcto.")
        seguir = input ("¿quieres seguir jugando? (s/n): ")
        seguir = seguir.lower()
    if seguir == "s":
        return False
    else:
        return True
        
    
 
def entroCueva(cueva):
    global puntuacion
    print ("Entro en la cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante mío, abre su boca y...")
    time.sleep (2)
    print ("¡¡emoción e intriga!!")
    time.sleep (3)
    dragon = random.randint (1,2)
    if dragon == cueva:
        print ("¡¡ Me entrega su tesoro !!")
        puntuacion += 100
    else:
        print ("Me zampa de un bocado con corcel y todo")
        print ("")
        print ("Tu puntuación es de: "+str(puntuacion)+" puntos")

        
    
    
def elegirCueva():
    print ("Elige cueva: izquierda (i) o derecha (d) ")
    cueva = input()
    cueva = cueva.lower()
    while cueva == "" or cueva.isspace() or cueva.isdigit() or ((cueva != "i") and (cueva != "d")):
        print ("El valor introducido no es correcto.")
        cueva = input ("Elige de nuevo la cueva: ")
        cueva = cueva.lower()
    
    if cueva =="i":
        cueva = 1
    elif cueva =="d":
        cueva = 2
    return cueva
            
    

def galopoPorElBosque():
    print ("")
    print ("-------------------------------------------------------" )
    print ("")
    print ("Voy galopando en mi corcel por el frondoso bosque")
    print("")
    time.sleep (2)
    print ("A lo lejos avisto dos cuevas una muy cerca de la otra")
    print ("")
    time.sleep (2)
    print ("Me acerco y ya las veo mejor. Una a mi izquierda y otra a mi derecha")
    print ("")
    time.sleep (2)
    print ("Tengo que escoger a cual quiero entrar")
    print("")
    time.sleep (3)
    cueva = elegirCueva()
    return cueva
    
fin_juego = False
introduccion()

while not fin_juego:
    cueva = galopoPorElBosque ()
    entroCueva(cueva)
    fin_juego = seguirJugando()
    
    


