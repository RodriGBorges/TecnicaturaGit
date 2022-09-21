"""

 Ejercicio 01 : Crear una función para sumar los valores recibidos de tipo
 numéricos , utilizando argumentos variables * args como parametro de la
 Función y agregar como resultado la suma de todos los valores pasados cono argumentos.

"""
# Definimos una función
def sumarValor (*args): # Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la función
print(sumarValor (3, 5, 9, 2, 1))