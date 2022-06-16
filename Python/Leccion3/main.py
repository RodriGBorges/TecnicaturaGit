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