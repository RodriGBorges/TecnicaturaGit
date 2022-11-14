from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))

print('.:CUADRADO:.')
cuadrado1 = Cuadrado(8, 'Rojo')
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcularArea()}')
print(cuadrado1)

print('')
# print('.:MRO:.')
#  MRO = Method Resolution Order
# Nos muestra el orden de las clases
# print(Cuadrado.mro())

print('')
print('.:RECTÁNGULO:.')
rectangulo1 = Rectangulo(3, 9, 'Azul')
rectangulo1.ancho = 8
# print(rectangulo1.ancho)
# print(rectangulo1.alto)
print(f'Cálculo del área del rectángulo: {rectangulo1.calcularArea()}')

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta
