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


# Clase 2 #

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


# --------------------------------------------------- #
# Diccionario #

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

# ------------------------------------------------------ #

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

# -------------------------------------------------------------------- #
# Repaso de Tuplas
tupla = (4, 'Hola Mundo', 6.78, [1, 2, 78], 4, 'Hola Mundo')
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len