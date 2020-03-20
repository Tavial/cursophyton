'''
Los tramos impositivos para la declaración de la renta en un determinado país 
son los siguientes:

Renta                    Tipo impositivo
Menos de 10000€            5%
Entre 10000€ y 20000€      15%
Entre 200000€ y 35000€     20%
Entre 350000€ y 60000€     30%
Más de 60000€              45%

Escribir un programa que pregunte al usuario su renta anual y muestre por 
pantalla el tipo impositivo que le corresponde.

'''
print (" ************************************************************  ")
print ("  Este programa muestra el tipo impositivo según renta anual ")
print (" ************************************************************ ")
print ("")
print (" Introduce tu renta anual: ")
renta = input()
if (renta=="") or renta.isspace() or renta.isalpha():
    print ("El valor introducido para la renta no es correcto")
else: 
    renta = float (renta)
    if (renta >= 0) and (renta < 10000):
        print ("Tu tipo impositivo es del 5%")
    elif (renta >= 10000) and (renta < 20000):
        print ("Tu tipo impositivo es del 15%")
    elif (renta >= 20000) and (renta < 35000):
        print ("Tu tipo impositivo es del 20%")
    elif (renta >= 35000) and (renta < 60000):
        print ("Tu tipo impositivo es del 30%")
    elif (renta >= 60000):
        print ("Tu tipo impositivo ed del 45%")
    else: 
        print ("El valor introducido de la renta es inferior a 0 ")
    