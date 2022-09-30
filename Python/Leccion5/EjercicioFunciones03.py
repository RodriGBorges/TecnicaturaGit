"""

 Ejercicio 03 : Función recursiva
 Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
 Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor 5, debe imprimir:
 5
 4
 3
 2
 1
 En caso de ser el número 3 debe imprimir:
 3
 2
 1
 Si se ingresan números negativos no imprime nada

"""

def imprimirNumerosRecursivos(numero):
    if numero >= 1:
        print(numero)
        imprimirNumerosRecursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto')

numero = int(input('Ingrese un número: '))
imprimirNumerosRecursivos(numero)