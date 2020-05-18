'''
Debido a la crisis, el bar de Javier ha notado un descenso de las consumiciones. Además, según dicen en los telediarios,
la ley antitabaco le está perjudicando aún más. Como no termina de creerse todo lo que dicen en la televisión, ha 
decidido hacer un estudio de mercado semanal de su establecimiento. Para ello, ha estado apuntando la caja diaria que se 
ha realizado en las últimas semanas. Le gustaría saber qué día de la semana se producen el mayor y el menor número de 
ventas, y si las ventas del domingo superan a la media semanal. De esta manera podrá establecer estrategias de marketing 
que le permitan recuperar algo de las ganancias perdidas.

Javier abre su bar todos los días menos los Lunes, que utiliza para descansar.

Realiza un programa que ayude a Javier en su cometido. Dada una lista de valores correspondiente a una semana, 
nuestro programa deberá decirle a Javier el día de la semana que más y menos ha vendido, y si las ventas del domingo 
superan la media.

ENTRADA -> El programa recibirá una lista de semanas a evaluar. Cada semana constará de un valor para cada día. El 
número de semanas es indeterminado. El programa terminará de ejecutarse cuando para el primer día de la semana se 
indique una venta de -1.

SALIDA -> Para cada caso de prueba, el programa escribirá una línea conteniendo dos días de la semana (MARTES, 
MIERCOLES, JUEVES, VIERNES, SABADO o DOMINGO). El primero indicará el día de más ventas y el segundo el de menos. 
Después se indicará un SI si el domingo se realizaron más ventas que la media semanal, y NO en caso contrario. Las tres 
palabras se separarán entre ellas por un espacio.

Si hay empate en alguno de los valores de ventas mínimo y máximo, se especificará EMPATE.

'''
from modulos.operaciones import Operaciones

archivo_entrada = open ("entrada.txt","r")
archivo_salida = open ("salida.txt","a")
lineas = archivo_entrada.read()
lineas = lineas.split("\n")

operacion = Operaciones()
i = 0
if lineas[0] == "-1":
    print ("Archivo sin entradas")
else: 
    while lineas[i] != "-1":
        semana = []
        dia = 1
        while dia < 7:
            if lineas[i] != "-1":
                semana.append(float(lineas[i]))
            i += 1
            dia += 1 
        print (semana)
        maximo = operacion.mayor(semana)
        minimo = operacion.menor(semana)
        media_semanal = operacion.mediaSemanal (semana)
        texto = maximo+" "+minimo+" "+media_semanal+"\n"
        archivo_salida.write (texto)
archivo_entrada.close()
archivo_salida.close()
