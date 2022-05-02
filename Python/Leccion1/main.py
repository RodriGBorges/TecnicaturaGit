#  Clase 1  #

"""
print('Hola Mundo')
"""

#  Clase 2  #

# Variables en Python

"""
# ¡¡ Una literal es un valor que podemos asignar a nuestras variables !!

# miVariable = 3
# print(miVariable)
# dato tipo int

# miVariable = "Hola a todos los estudiantes de la tecnicatura"
# print(miVariable)
# dato tipo string

# miVariable = 3.5
# dato tipo float
# print(miVariable)

x = 10
y = 2
z = x + y
# print(id(x))

# Las literales se escriben de la siguiente manera x___
# X seguido de los ultimos 3 digitos de la memoria: ejemplo = "x104"
# Las literales cambian constantemente, el id no es estático

print(id(x))
print(id(y))
print(id(z))

# En este ejemplo x=248 y=992 z=312, si se hace otra vez sus valores cambian
# A esto se lo conoce como referencia de memoria o simplemente referencia

"""

#  Clase 3  #

# Tipos de datos int, string, float, bool

"""

a = "Hola alumnos"
# print(type(a))
# Tipo Stri

a = 10
# print(type(a))
# Tipo Int

a = 10.78
# print(type(a))
# Tipo Float

a = True
print(type(a))
# Tipo Bool / a diferencia de js la primer letra va con mayúscula True - False

----------------------------

# Manejo de caracteres 

# miGrupoFavorito = "Daft Punk"
# print("Mi grupo favorito es: " + miGrupoFavorito + " - " + "The Best Pop Band")

# miGrupoFavorito = "Daft Punk - ""The Best Pop Band"
# print("Mi grupo favorito es: " + miGrupoFavorito)

# miGrupoFavorito = "Daft Punk - "
# caracteristicas = "The Best Pop Band"
# print("Mi grupo favorito es: " + miGrupoFavorito + caracteristicas)

miGrupoFavorito = "Daft Punk - "
caracteristicas = "The Best Pop Band"
# print("Mi grupo favorito es: ",miGrupoFavorito, caracteristicas)


numero1 = "7"
numero2 = "8"
# print(numero1 + numero2)

# Se pueden sumar cadenas siempre y cuando sean del mismo dato
# print(int(numero1) + int(numero2))


# Tipos Boleanos (bool)
miBooleano = 3 > 2
# print(miBooleano)

if miBooleano:
    print("El resultado es true")
else:
    print("El resultado es false")

----------------------------------------

# Procesar la entrada del usuario

# función input
# resultado = input("Digite un número: ") # regresa un dato tipo string
# print(resultado)


# Conversión de la entrada de datos

numero3 = int(input("Escribe el primer número: "))
numero4 = int(input("Escribe el segundo número: "))
resultado1 = numero3 + numero4
print("El resultado de la suma es: ", resultado1)

"""
# Ejercicio 1 #

"""


# Califica tu día
print("Como estuvo tu día del 1 al 10?")
resultado = input("Digite un número: ")
print("Mi día estuvo de: " + resultado)

"""

# Ejercicio 2 #

"""
# Se solicita incluir la siguiente información acerca de un libro:
titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor del libro: ")
print(titulo + " de " + autor)

"""