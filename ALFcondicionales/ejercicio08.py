'''
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir 
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir 
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre 
las cifras mencionadas. A continuación se muestra una tabla con los niveles 
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada 
nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel        Puntuación
Inaceptable    0.0
Aceptable      0.4
Meritorio      0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de 
rendimiento, así como la cantidad de dinero que recibirá el usuario.

'''
print (" ****************************************************** ")
print ("  Calculo del nivel de rendimiento y dinero percibido")
print (" ****************************************************** ")
print ("")
print ("Introduzca su puntuación 0.0, 0.4, 0.6, 0.8 o 1: ")
puntuacion = input ()
if puntuacion =="" or puntuacion.isspace() or puntuacion.isalpha():
    print ("El valor introducido no es numérico")
else: 
    puntuacion = float (puntuacion)
    prima = 2400 * puntuacion
    if puntuacion == 0.0:
        print ("Tu nivel de rendimiento es Inaceptable y la prima que recibirás es: "+str(prima)+" euros")
    elif puntuacion == 0.4:
        print ("Tu nivel de rendimiento es Aceptable y la prima que recibirás es: "+str(prima)+" euros")
    elif puntuacion >= 0.6 and puntuacion <= 1:
        print ("Tu nivel de rendimiento es Meritorio y la prima que recibirás es: "+str(prima)+" euros")
    else: 
        print ("El valor de la puntuación introducido no es correcto")
