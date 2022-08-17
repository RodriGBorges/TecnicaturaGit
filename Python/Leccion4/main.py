# Lista = Ariel, Liliana, Natalia, Osvaldo

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

# Agregamos un elemento
nombres.append('Marcelo')
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
