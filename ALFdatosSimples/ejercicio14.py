'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día 
tiene un descuento del 60%. Escribir un programa que comience leyendo el número 
de barras vendidas que no son del día. Después el programa debe mostrar el precio 
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el 
coste final total.

'''
descuento_nofresco = 60
precio_barra = 3.49
n_barras = int (input("Introduce el número de barras vendidas que no son frescas: "))
precio = round (((precio_barra*n_barras*descuento_nofresco)/100),2)
print ("El precio habitual de la barra fresca es de "+str(precio_barra)+" euros")
print ("El pan vendido al no ser fresco tiene un descuento del "+str(descuento_nofresco)+"%")
print ("El precio total del pan vendido que no es fresco es de: "+str(precio)+" euros")