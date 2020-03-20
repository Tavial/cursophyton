'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece 
el 4% de interés al año. Estos ahorros debido a intereses, que no se 
cobran hasta finales de año, se te añaden al balance final de tu 
cuenta de ahorros. Escribir un programa que comience leyendo la 
cantidad de dinero depositada en la cuenta de ahorros, introducida 
por el usuario. Después el programa debe calcular y mostrar por 
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.

'''
balance = float (input("Introduce el saldo de tu cuenta de ahorros: "))
balance_1anyo = round ((balance + balance*0.04),2)
balance_2anyos = round ((balance_1anyo + balance_1anyo*0.04),2)
balance_3anyos = round ((balance_2anyos + balance_2anyos*0.04),2)
print ("Saldo en tu cuenta en el primer año: "+str(balance_1anyo)+" euros")
print ("Saldo en tu cuenta en el segundo año: "+str(balance_2anyos)+" euros")
print ("Saldo en tu cuenta en el tercer año: "+str(balance_3anyos)+" euros")
