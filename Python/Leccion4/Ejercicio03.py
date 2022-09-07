# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

lista = []
salir = False # bandera
# mientras salir no sea verdadero
while not salir:
    numero = int(input('Ingrese un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # la lista está ordenada con esta función
print(f'\nLista ordenada: \n{lista}')