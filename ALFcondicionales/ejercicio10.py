'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus 
clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o 
no, y en función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir un ingrediente además de la 
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes 
que lleva.

'''
print (" ************************ ")
print ("  Pizzeria Bella Napoli  ")
print (" ************************ ")
print ("")
print ("¿Quieres que tu pizza sea vegetariana? (S/N): ")
eleccion = input ()
if eleccion == "" or eleccion.isspace() or eleccion.isdigit():
    print ("El valor introducido no es correcto")
else: 
    eleccion = eleccion.lower()
    if eleccion =="s":
        print ("Su pizza vegetariana tiene una base de tomate y mozzarella.")
        print ("Elija uno de los siguientes ingredientes: ")
        print ("a. Pimiento     b. Tofu")
        eleccion_v = input()
        if eleccion_v == "" or eleccion_v.isspace() or eleccion_v.isdigit():
            print ("El valor introducido no es correcto")
        else: 
            eleccion_v = eleccion_v.lower()
            if eleccion_v == "a":
                print ("Pasamos a cocina su pedido con los siguientes ingredientes:")
                print ("Tomate, mozarella y pimiento")
            elif eleccion_v == "b":
                print ("Pasamos a cocina su pedido con los siguientes ingredientes:")
                print ("Tomate, mozarella y tofu")
            else: 
                print ("No ha introducido una opción correcta")
    elif eleccion == "n":
        print ("Su pizza (no vegetariana) tiene una base de tomate y mozzarella.")
        print ("Elija uno de los siguientes ingredientes: ")
        print ("a. Peperoni     b. Jamón    c. Salmón")
        eleccion_nv = input()
        if eleccion_nv == "" or eleccion_nv.isspace() or eleccion_nv.isdigit():
            print ("El valor introducido no es correcto")
        else: 
            eleccion_nv = eleccion_nv.lower()
            if eleccion_nv == "a":
                print ("Pasamos a cocina su pedido con los siguientes ingredientes:")
                print ("Tomate, mozarella y peperoni")
            elif eleccion_nv == "b":
                print ("Pasamos a cocina su pedido con los siguientes ingredientes:")
                print ("Tomate, mozarella y jamon")
            elif eleccion_nv == "c":
                print ("Pasamos a cocina su pedido con los siguientes ingredientes:")
                print ("Tomate, mozarella y salmón")
            else: 
                print ("No ha introducido una opción correcta")
    else: 
        print ("La opción introducida no tiene un valor correcto (s/n)")
    
    
    
