from abc import ABC, abstractmethod


# abc => Abstract Base Class, convierte una clase en abstracta

class FiguraGeometrica(ABC):  # FiguraGeometrica va a ser hija de ABC aparte de la de object
    def __init__(self, ancho, alto):
        # Validaciones
        if self._validarValores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validarValores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validarValores(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validarValores(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validarValores(self, valor):  # Método encapsulado
        return True if 0 < valor < 10 else False
