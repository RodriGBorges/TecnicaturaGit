# Clase 4 #

# Ejercicio 1:Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

"""
lista1 = {1, 8, 3, 3, 4, 5, 5, 7}
lista2 = {6, 7, 7, 8, 2, 9, 6, 4}
print("Lo que hay en las listas: ")
conjunto1 = lista1 | lista2 # La línea une a los dos conjuntos, si hay datos iguales se borran y queda 1 solo
print(conjunto1)
print("")

print("Lo que aparece en la primera pero no en la segunda: ")
conjunto2 = lista1 - lista2 # Asigna el valor que está en el conjunto1 y no en el conjunto2
print(conjunto2)
print("")

print("Lo que aparece en la segunda pero no en la primera: ")
conjunto3 = lista2 - lista1 # mismo pero al revés
print(conjunto3)
print("")

print("Elementos en común")
conjunto3 = lista1 & lista2 # elementos que tienen en común
print(conjunto3)
"""

# forma profe
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

# eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) # Mostramos elementos que coinciden ambas listas

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")