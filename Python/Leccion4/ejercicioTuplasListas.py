import math # Importamos la clase math para hacer uso de la función sqrt(raiz cuadrada)
# Dada la siguiente tupla
"""
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]

nuevaListaTupla = [] # Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for tupl in tupla:
    if(tupl < 5):
        nuevaListaTupla.append(tupl)
        print(f'Se agrega {tupl}')
    else:
        print(f'El número {tupl} no cumple con la condición')

print(f'Se terminaron de filtrar los números, la nueva lista contiene: ')
print(nuevaListaTupla)
"""

# ------------------------------------------------------------------------------------------------------- #
# Clase 4 #

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo nuevamente: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')
# .2f para que no nos tire un número largo y solo se muestren 2 digitos