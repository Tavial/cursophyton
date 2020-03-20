'''
Escribir un programa que pregunte al usuario por el número de horas trabajadas y
 el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

'''
horas_trabajadas = float (input ("Introduce el número de horas trabajadas: "))
coste_hora = float (input ("Introduce en euros el precio por hora: "))
paga = round ((horas_trabajadas * coste_hora),2)
print ("La paga que te corresponde es: "+str(paga)+" euros")
                        