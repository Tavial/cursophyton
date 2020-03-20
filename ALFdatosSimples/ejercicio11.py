'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
anual y el número de años, y muestre por pantalla el capital obtenido en la 
inversión.

Capital final = Capital inicial * interes anual * numero de años.

'''
print (" Vamos a calcular el capital obtenido en una inversión")
print ("")
capital_ini = float (input("Introduce el capital inicial: "))
interes_anual = float (input("Introduce el interés anual (en %): "))
anios = float (input ("Introduce el número de años: "))
capital_fin =round ((capital_ini*interes_anual*anios/100),2)
print ("El capital obtenido en la inversion es: "+str (capital_fin))

