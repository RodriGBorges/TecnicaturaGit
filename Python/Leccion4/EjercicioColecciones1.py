# Clase 4 #

# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista
# forma 1
"""
lista = ['Bananas', 'Manzanas', 'Peras', 'Frutillas', 'Frutillas', 'Bananas', 'Ciruelas', 'Ananas', 'Ananas', 'Duraznos']
print(lista)
filtro = []

for fruta in lista:
    if fruta not in filtro:
        filtro.append(fruta)

print(f'La lista filtrada sería: {filtro}')
"""
# forma 2, profe
"""
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel"]
conjunto = set(lista)
print(conjunto)
"""
# forma 3, profe

lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel", 2, "Alberto"]
"""
conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
lista = list(conjunto) # Convertimos el conjunto a una lista
print(lista)
"""
# forma 4, simplificada (eficiente)
lista = list(set(lista))
print(lista)