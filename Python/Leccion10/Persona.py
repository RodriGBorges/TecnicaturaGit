class Persona:
    contadorPersonas = 0  # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorPersonas += 1  # Se va incrementando
        return cls.contadorPersonas

    def __init__(self, nombre, edad):
        self.idPersona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [ID: {self.idPersona}, NOMBRE: {self.nombre}, EDAD: {self.edad}]'


persona1 = Persona('Lucifer', 36)
print(persona1)
persona2 = Persona('Amenadiel', 34)
print(persona2)
persona3 = Persona('Gabriel', 32)
print(persona3)

Persona.generar_siguiente_valor()  # Aumento de id

persona4 = Persona('Uriel', 30)
print(persona4)

print(f'Valor contador personas: {Persona.contadorPersonas}')