# Clase 8 #
"""
class Persona: # Creamos una clase
    pass # No se procesa nada más

print(type(Persona))

"""


class Persona:
    def __init__(self, nombre, apellido, edad):  # Método Init Dunder /
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, {self.edad} años')


persona1 = Persona('Ariel', 'Betancud', 40)  # Le enviamos los argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Bucella'
persona1.edad = 40

print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: características
# Los métodos son: El comportamiento que van a tener los objetos (acciones)

persona1.mostrarDetalle()
persona2.mostrarDetalle()
