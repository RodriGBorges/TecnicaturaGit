from Color import Color
from FiguraGeometrica import FiguraGeometrica


# El orden de importacion es importante
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado) / No se usa super en herencia multiple porque no se sabe a que padre va a acudir para el atributo
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'