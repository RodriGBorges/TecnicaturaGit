# Lista = Ariel, Liliana, Natalia, Osvaldo

# Colecciones en Python #

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
"""
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
# Inversa usando números negativos
print(nombres[-1]) # -1 arranca del último hacia el primero
print(nombres[-2])

"""

"""
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # indices a mostrar 0, 1, 2

# Desde el indice indicado hasta el final
print(nombres[1: ])

# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista
for nombre in nombres: # Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres))# le pasamos como parametro la lista

# Agregamos un elemento / puede ser una lista de elementos, booleano o tipo float
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) # Aquí nos mostrará un error

# Las tuplas son inmutables, no se pueden modificar
# Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes, no parentesis
print(cocina[0])
# Forma inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2]) # El segundo numero siempre es uno menos

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo sería un tipo str cadena

# Recorremos los elementos de una tupla
for cocinar in cocina: # Print esta usando por defecto \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de lineas

# cocina[0] = 'plato'
# print(cocina)
# no se puede modificar la tupla

# La única forma de modificar la tupla es pasando de tupla a lista y de lista a tupla
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina) # Con \n anulamos el end anterior

# del cocina # esto es para eliminar la tupla
"""

# ------------------------------------------------------------------------------------------------------ #
# Clase 2 #
"""
# Tipo set o conjunto (nos puede servir para evitar en una lista los datos duplicados ej: dni, matrícula)
# No tienen índice fijo, van cambiando de forma aleatoria
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Len = largo

# Revisar si un elemento existe dentro de set
print('Júpiter' in planetas) # Respetar tildes, mayúsculas y minúsculas

# Agregar un elemento (no se pueden agregar elementos duplicados o repetidos)
planetas.add('Tierra') # add = agregar
print(planetas)

# Eliminar elementos (tira error si el elemento no existe)
planetas.remove('Tierra')
print(planetas)

# discard en cambio, no tira error si el elemento no está
planetas.discard('Martes')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas

"""
# -------------------------- #
# Diccionario #
"""
# 'Maradona':10 / Un diccionario está compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE']) # Respetar tildes, mayúsculas y minúsculas

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos

for termino in diccionario:
    print(termino) # Solo accedemos a las llaves

# Necesitamos una funcion para recorrer un diccionario = items()
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Solo accedemos a las llaves

for valor in diccionario.values():
    print(valor) # Solo accedemos a los valores

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve booleano

# Agregar un elemento
# No se pueden duplicar datos, si ya existe se va a reemplazar por el existente
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
"""
# -------------------------- #
"""
# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

# Función para agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1])
print(lista3)

# Función para ubicar en que índice está el valor ingresado
print(lista3.index(5))
# print(lista3.index(0)) # Esto da error ya que no está en la lista

# Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))

# Para poner la lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
# lista = [1, 2, 3] * 2
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento con funciones
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)

lista3.sort(reverse=True) # Descendente
print(lista3)
"""
# -------------------------- #
"""
# Repaso de Tuplas
tupla = (4, 'Hola Mundo', 6.78, [1, 2, 78], 4, 'Hola Mundo')
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
"""
# --------------------------------------------------------------------------------------------------- #
# Clase 3 #

# Para definir un conjunto
"""
conjunto1 = set() # la única manera de inicializar un conjunto es con la funcion set

# conjunto1 = {} Con las llaves solas no se puede empezar un conjunto porque ya fue inicializado
conjunto2 = {'bye', } # si queremos inicializarlo con llaves debemos inicializarlo con un elemento dentro y despues
# podemos ir agregando más elementos

conjunto1.add(7)
conjunto1.add('Hola')
print(conjunto1)

conjunto2.add('hola')
print(conjunto2)
print(3 not in conjunto2) # preguntamos si el número 3 NO está en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une a los dos conjuntos, si hay datos iguales se borran y queda 1 solo
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3) # Si 1 y 2 poseen 'Hola' se va a guardar aquí

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 # mismo pero al revés
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2 # Si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Si los elementos de conjunto1 están dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se pueden agregar, modificar o eliminar elementos del conjunto

# listas{} son mutables, siguen un orden, saca elementos repetidos
# tuplas() son inmutables, son desordenadas
# diccionario{} lleva una llave y un valor, siguen un orden
# set{} mutables e inmutables, son desordenadas
"""
# -------------------------- #
"""
# Repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)
"""
# -------------------------- #
# Ejercicio
"""
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'}
}

seleccionArgentina[23] = {'Nombre': 'Javier Mascherano', 'Edad': 38, 'Altura': 1.74, 'Precio': '30 Millones', 'Posicion': 'Defensa Central'}
seleccionArgentina[20] = {'Nombre': 'Emiliano Martinez', 'Edad': 29, 'Altura': 1.95, 'Precio': '28 Millones', 'Posicion': 'Portero'}
seleccionArgentina[12] = {'Nombre': 'Carlos Tevez', 'Edad': 38, 'Altura': 1.71, 'Precio': '40 Millones', 'Posicion': 'Mediapunta'}
seleccionArgentina[13] = {'Nombre': 'Rodrigo de Paul', 'Edad': 28, 'Altura': 1.80, 'Precio': '40 Millones', 'Posicion': 'Mediocentro'}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Otra forma de mostrar
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

"""
# -------------------------- #

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacar elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output) primero en entrar / primero en salir

cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
