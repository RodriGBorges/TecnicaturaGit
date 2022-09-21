# Clase 5 #
# Comenzamos con funciones

# Definimos una función
def miFuncion(): # Para identificar a la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura")

miFuncion() # Estamos llamando a la función
miFuncion() # Se puede llamar a una función X cantidad de veces


# ----------------------------------------------------------------------------------------- #
# Clase 6 #
# Desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name + ' ' + lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aún con la lista vacía se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la única manera para que no se ejecute el else
    else:
        print('Esto se termino')


# List comprehension, lista de compresión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Paso de argumentos (funciones)
def miFuncion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
miFuncion2('Jorge', 'Lucero')
miFuncion2('Ariel', 'Betancud')
miFuncion2('Analia', 'Pedrosa')


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')


# def sumar2(a:int = 0, b:int = 0)
def sumar2(a = 0, b = 0) -> int: # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
# no sabemos cuantos argumentos le vamos a pasar a la función, asi que lo expresamos con este parámetro
def listarNombres(*nombres): # Normalmente se utiliza: *arg
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')