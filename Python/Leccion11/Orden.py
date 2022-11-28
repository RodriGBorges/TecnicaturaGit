from Producto import Producto


class Orden:
    contadorOrdenes = 0

    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        self.idOrden = Orden.contadorOrdenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)  # Append para agregar un nuevo producto

    def calcular_total(self):
        total = 0  # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio

        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+' | '

        return f'Orden: {self.idOrden}, \nProducto: {productos_str}'

