# Clase 4 #

# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes
# Nombre: Ainz Ooal Gown
# Clase: Mago
# Raza: No Muerto

# Nombre: Albedo
# Clase: Tanque
# Raza: Súcubo

# Nombre: Demiurge
# Clase: Guerrero
# Raza: Demonio

personajes = [] # Creamos una lista vacía

# Creamos diccionarios

P = {'Nombre': 'Ainz Ooal Gown', 'Clase': 'Mago', 'Raza': 'No Muerto'}
personajes.append(P) # agregamos a la lista un personaje
P = {'Nombre': 'Albedo', 'Clase': 'Tanque', 'Raza': 'Súcubo'}
personajes.append(P)
P = {'Nombre': 'Demiurge', 'Clase': 'Guerrero', 'Raza': 'Demonio'}
personajes.append(P)

print(personajes) # Tarea: Agregar por lo menos otros tres personajes