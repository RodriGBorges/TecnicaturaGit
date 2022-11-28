class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, otro):  # Sub => Substraction (resta)
        return self.edad - otro.edad



persona1 = Persona('Rodrigo', 20)
persona2 = Persona('Borges', 2)

#  persona1.__add__(persona2) sintaxis interna y automática

print(persona1 + persona2)
print(persona1 - persona2)