'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales. 
IMC = peso(kg) /Estatura al cuadrado (en metros) 

'''
peso = float (input("Introduce tu peso en kg.: "))
estatura = float (input("Introduce tu estatura en metros: "))
imc = round((peso/pow(estatura,2)),2)
print ("Tu índice de masa corporal es: "+str(imc))