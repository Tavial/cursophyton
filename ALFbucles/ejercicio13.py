'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
hasta que el usuario escriba “salir” que terminará.

'''
salir = False
print ("")
print ("-----------------------------------------------")
print ("| Soy el ECO. Para salir escribe 'salir'      |") 
print ("|(no distingue entre mayúsculas y minúsculas) |")
print ("-----------------------------------------------")
while not salir: 
    eco = input()
    verifica = eco.lower()
    if verifica == "salir": # salimos cuando el usuario escriba la palabra salir
        print ("Adiós !!")
        salir = True
    else:
        print (eco)

    