class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y métodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hr))
    -Métodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Métodos(__init__(color, ruedas, tipo) y __str__()

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color}, Ruedas: {str(self.ruedas)}'


class Auto(Vehiculo): # Clase auto herendando de la clase Vehiculo (pasa a ser hija)
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {str(self.velocidad)}km/h'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'


# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 6)
print(vehiculo)

# Segundo objeto de la clase Auto
auto = Auto('Azul', 4, 120)
print(auto)

# Tercer objeto de la clase Bicicleta
triciclo = Bicicleta('Verde', 3, 'Infantil')
print(triciclo)