# Clase 8 #
# Ciclo while (mientras o durante)
"""
contador = 0
while contador < 5:
    print(f'Ejecutamos nuestro ciclo while {contador}')
    contador += 1
else:
    print('Fin del ciclo while')
"""

"""
# Imprimir números del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
"""

"""
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
"""

# Ciclo for

"""
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')
"""

# Va a seguir hasta finalizar la cadena

"""
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
else:
    print('Fin del ciclo for')
"""

# Palabra reservada break (apenas lo encuentre al primer elemento, rompe el ciclo)
"""
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')
"""

# Palabra reservada continue
"""
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')
"""
# Continue: eludir / anular todos los números que sean impares
"""
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
"""

# Clase 9 #

# Diseñar un programa que ingresado un año, nos devuelva por consola si es un año bisiesto o no, repetir
# la acción hasta que el usuario lo desida.

"""
opcion = 1
print('Comprobamos que año es bisiesto')
while opcion == 1:
    num = int(input('Ingrese el año: '))
    if (num % 4 == 0) and (num % 100 != 0) or num % 400 == 0:
        print('El año es Bisiesto')
    else:
        print('El año no es Bisiesto')
    opcion = int(input('Para seguir adelante digite la opcion 1: '))
else:
    print('Fin del programa')
"""

# Calcular la suma de "n" primeros números

"""
n = int(input('Digite la cantidad de números a sumarse: '))
suma = 0
for i in range(n):
    print(f'Vuelta {i}')
    print(f'Se suma {suma} + {i}')
    suma += i
print(f'La suma es: {suma}')
"""

# Leer 10 números e imprimir cuantos son positivos, cuantos son negativos y cuantos neutros.
"""
conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(10):
    num = int(input(f'{i}_Digite un número: '))
    if num == 0:
        conteoNeutros += 1
    else:
        if num > 0:
            conteoPositivos += 1
        else:
            conteoNegativos += 1
print(f'La cantidad de positivos es: {conteoPositivos}')
print(f'La cantidad de negativos es: {conteoNegativos}')
print(f'La cantidad de neutros es: {conteoNeutros}')
"""

# Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos. Realizar un algoritmo para calculcar
# la calificación promedio y la calificación más baja de todod el grupo.

"""
calificacionPromedio = 0
calificacionBaja = 99999
calificacionSuma = 0
suma = 0

for i in range(10):
    calificacion = float(input(f'{i}_Digite una calificacion: '))
    # Suma interactiva de las calificaciones
    suma = suma + calificacion
    # Calcular la menor calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
calificacionPromedio = suma / 10
print(f'La calificación promedio es: {calificacionPromedio}')
print(f'La calificacion más baja es: {calificacionBaja}')
"""

# Clase 10 #

# Ejercicio 5: Calcular el factorial de un número mayor o igual a 0

"""
for x in range(9999):
    num = int(input('Digite un número: '))
    if num >= 0:
        break

i = 1
factorial = 1

while i <= num:
    print(f'{factorial} * {i} = ', end=" ")
    factorial *= i
    print(f'{factorial}')
    i += 1

print(f'\nEl factorial es: {factorial}')

"""

# Ejercicio 6: Ingresar "n" enteros, visualizar la suma de los números pares de la lista, cuántos números pares
# existen y cuál es el promedio de los números impares.

"""
nElementos = int(input('Digite la cantidad de elementos a ingresar: '))

i = 1
sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0

while i <= nElementos:
    num = int(input(f'{i}_Digite un número: '))
    if num % 2 == 0:
        sumaPares += num
        conteoPares += 1
    else:
        sumaImpares += num
        conteoImpares += 1
    i += 1

if conteoPares == 0:
    print('No se han digitado números pares')
else:
    print(f'\nLa suma de los números pares es: {sumaPares}')
    print(f'El conteo de los números pares es: {conteoPares}')

if conteoImpares == 0:
    print('No se han digitado números impares')
else:
    promedioImpares = sumaImpares / conteoImpares
    print(f'\nLa suma de los números impares es: {sumaImpares}')
    print(f'El conteo de los números impares es: {conteoImpares}')
    print(f'El promedio de impares es: {promedioImpares}')
"""

# Ejercicio 7: Dadas las horas trabajadas de 5 personas y la tarifa de pago, calcular el salario, y la sumatoria
# de todos los salarios

"""
i = 1
suma = 0

while i <= 5:
    print(f'Salario del empleado {i}: ')
    horas = float(input('Digite las horas trabajadas: '))
    tarifa = float(input('Digite la tarifa por hora: '))
    salario = horas * tarifa
    print(f'El salario es: ${salario}')
    suma = suma + salario
    i += 1
    print('')

print(f'La suma de todos los salarios es: ${suma}')
"""