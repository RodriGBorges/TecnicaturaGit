from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('.:CUADRADO:.')
cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)

print('')
print('.:MRO:.')
#  MRO = Method Resolution Order
# Nos muestra el orden de las clases
print(Cuadrado.mro())

print('')
print('.:RECTÁNGULO:.')
rectangulo1 = Rectangulo(3, 8, 'Azul')
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(f'Cálculo del área del rectángulo: {rectangulo1.calcularArea()}')