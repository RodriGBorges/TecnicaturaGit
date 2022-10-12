class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un método CalcularVolumen que tendrá
    la formula:
    volumen = ancho * altura * profundidad
    pedir que el usuario ingrese los valores
    """

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input('Ingrese el número para el ancho del cubo: '))
altura = int(input('Ingrese el número para la altura del cubo: '))
profundidad = int(input('Ingrese el número para la profundidad del cubo: '))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')