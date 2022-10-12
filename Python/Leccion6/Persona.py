# Clase 8 #
"""
class Persona: # Creamos una clase
    pass # No se procesa nada más

print(type(Persona))

"""

# *args => argumentos para tuplas / **kwargs => argumentos para diccionarios
class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Método Init Dunder /
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida / con __dni queda totalmente encapsulado, no se puede modificar
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self): # self es igual a this
        #  print(f'Persona: {self.nombre} {self.apellido}, {self.edad} años')
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni}, {self.edad} años, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud', 32456987, 40)  # Le enviamos los argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 32456987, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Bucella'
persona1.edad = 40

print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: características
# Los métodos son: El comportamiento que van a tener los objetos (acciones)

persona1.mostrarDetalle() # La referencia en este caso se pasa de manera automática
persona2.mostrarDetalle()

# Persona.mostrarDetalle() # Debemos pasarle una referencia para el self o dará error

persona1.telefono = '44445555289'
# print(persona1.telefono) # Hemos creado un atributo de un objeto (solo para persona1, dato superficial)
print(f'Este es el teléfono de: {persona1.nombre} {persona1.telefono}')

# print(persona2.telefono) # el objeto persona2 no tiene este atributo

persona3 = Persona('Rogelio', 'Romero', 32456987, 22, 'Teléfono', '2614445557', 'Calle Lopez', 833, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrarDetalle()
# print(persona3._dni) # esto no se debe utilizar(está encapsulado), esto dice que desconocemos python
# persona3.__dni # está totalmente encapsulado