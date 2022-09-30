"""

 Ejercicio 02 : Función con * arg para multiplicar
 Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args
 como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos

"""

def multiplicarValores(*args):
    resultado = 1 # El cero no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado

# Llamamos a la función

print(multiplicarValores(3, 5, 15, 3)) # Le pasamos los argumentos