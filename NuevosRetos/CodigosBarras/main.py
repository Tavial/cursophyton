"""
-------------------------- RETO 1 - CÓDIGOS DE BARRAS  --------------------------------------------------

La manera concreta de codificar mediante barras los números y las letras puede ser muy variada, lo que ha 
llevado a la aparición de diferentes estándares. De todos ellos, el EAN (European Article Number) resulta 
ser el más extendido. De éste, hay principalmente dos formatos, que se diferencian en el ancho. Existe así 
el llamado EAN-8, que codifica 8 números, y el EAN-13, que, naturalmente, codifica 13.

El último dígito del código se utiliza para detección de errores, y se calcula a partir de los demás. Para eso:

* Empezando por la derecha (sin contar el dígito de control que se está calculando), se suman los dígitos 
  individuales, multiplicados por un factor:
    - Los dígitos en posiciones impares (empezando a contar por la derecha saltándonos el de control) se multiplican 
      por 3.
    - Los dígitos en posiciones pares se multiplican por 1.

  Por ejemplo, para el código EAN-8 de la figura la operación a realizar es:
  2 · 3 + 5 · 1 + 9 · 3 + 3 · 1 + 8 · 3 + 5 · 1 + 6 · 3 = 88
  
* El dígito de comprobación es el número que hay que sumar al resultado anterior para llegar a un valor múltiplo de 10. 
  En el ejemplo de EAN-8, para llegar al múltiplo de 10 más cercano por encima del número 88 hay que sumar 2 (y llegar 
  al 90). Ten en cuenta que si la suma resulta ser ya múltiplo de 10, el dígito de control será 0.

En EAN-13, los primeros dígitos se usan además para identificar al país. Ejemplo de tabla: 
                            539:Irlanda,
                            54:Bélgica & Luxemburgo,
                            560:Portugal,
                            569:Islandia,
                            57:Dinamarca,
                            590:Polonia,
                            84:España, etc...

La entrada estará formada por una serie de casos de prueba. Cada uno contendrá una sucesión de números pertenecientes 
a un código de barras EAN-8 o EAN-13, incluyendo el dígito de control. Si el número de dígitos es inferior a 8, se 
asumirá que es un código EAN-8; si es superior a 8 pero inferior a 13, se asumirá EAN-13. En ambos casos, se completarán 
el resto de dígitos colocando ceros a la izquierda.

El último caso de prueba es seguido por una línea con un 0 que no provoca salida.
   
Salida:
------
Para cada caso de prueba, el programa indicará si el dígito de control es correcto o no. 

Si el código de barras es EAN-13 y correcto, el programa escribirá además el país al que pertenece. Si el código no 
aparece en la tabla, el programa mostrará "Desconocido".  
                        

"""
from modulos.validacion import Codigo

#print ("Introduzca los dígitos del código de barras: ")
#codigo_de_barras = str(input()) #leemos por teclado el código de barras
archivo_entrada = open("entrada_codigos.txt","r") #abrimos el fichero para lectura.
archivo_salida = open ("resultados_codigos.txt","a")

codigo = Codigo () #definimos un objeto de la clase Codigo
contenido = str(archivo_entrada.read())
contenido = contenido.split("\n")
print (contenido)

for codigo_de_barras in contenido:
    codigo_ok = codigo.validarCodigoBarras(codigo_de_barras) #invocamos al metodo de la clase Codigo para que verifiqueque el código introducido es correcto
    if codigo_ok:
        tipo_codigo = codigo.tipoCodigo(codigo_de_barras)       
        codigo_de_barras = codigo.rellenarConEspacios(codigo_de_barras)# invocamos al método de la clase Código para que rellene los espacios que faltan hasta 8 o hasta 13 con 0's a la izquierda
        digito_control_ok = codigo.comprobarDigitoControl(codigo_de_barras)
        if digito_control_ok:
            texto = "El código "+codigo_de_barras+" es: "+tipo_codigo
            if len(codigo_de_barras) == 13:
                pais = codigo.comprobarPais(codigo_de_barras)
                texto = texto+" - País: "+pais
                texto = texto +" - Dígito de control correcto"+"\n"
            elif len(codigo_de_barras) == 8:
                if  codigo_de_barras == "00000000":
                    texto = texto +" -- FIN --"+"\n"   
                else:
                    texto = texto +" - Dígito de control correcto"+"\n"           
        else: 
            texto = texto +" - Dígito de control incorrecto"+"\n"
    else:
        texto = texto +" - El código "+codigo_de_barras+" NO es correcto"+"\n"
    archivo_salida.write (texto)
archivo_entrada.close()
archivo_salida.close()




