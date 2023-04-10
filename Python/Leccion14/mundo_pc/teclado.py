from mundo_pc.dispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contadorTeclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contadorTeclados += 1
        self._idTeclados = Teclado.contadorTeclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'id: {self._idTeclados}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'


# Pruebas
if __name__ == '__main__':
    teclado1 = Teclado('Genius', 'USB')
    print(teclado1)
    teclado2 = Teclado('Logitech', 'Bluetooth')
    print(teclado2)