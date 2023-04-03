from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):  # Este es el método para aprender lo que es polimorfismo
    # print(objeto)  # De manera indirecta llama al str de la clase Empleado o de la clase Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Rodrigo', 90000.00)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 150000.00, 'Sistemas')
imprimir_detalles(gerente)