from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('Samsung', 'USB')
monitor1 = Monitor('Samsung', '27 Pulgadas')
raton1 = Raton('Samsung', 'USB')
computadora1 = Computadora('Samsung', monitor1, teclado1, raton1)


teclado2 = Teclado('Lenovo', 'Bluetooth')
monitor2 = Monitor('Lenovo', '17 Pulgadas')
raton2 = Raton('Lenovo', 'Bluetooth')
computadora2 = Computadora('Lenovo', monitor1, teclado1, raton1)


teclado3 = Teclado('Gamer', 'USB')
monitor3 = Monitor('Gamer', '24 Pulgadas')
raton3 = Raton('Gamer', 'USB')
computadora3 = Computadora('Gamer', monitor1, teclado1, raton1)


teclado4 = Teclado('Apple', 'Bluetooth')
monitor4 = Monitor('Apple', '24 Pulgadas')
raton4 = Raton('Apple', 'Bluetooth')
computadora4 = Computadora('Apple', monitor1, teclado1, raton1)

teclado5 = Teclado('Noblex', 'USB')
monitor5 = Monitor('Noblex', '19 Pulgadas')
raton5 = Raton('Noblex', 'USB')
computadora5 = Computadora('Noblex', monitor1, teclado1, raton1)

computadora6 = Computadora('Samsung', monitor1, teclado2, raton4)
computadora7 = Computadora('Noblex', monitor2, teclado3, raton5)

computadoras1 = [computadora1, computadora2, computadora7, computadora4]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora5, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)
