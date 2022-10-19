from Persona2 import Persona2
# para importar todo *

# Comprobación del método principal en ejecución (de dónde se está ejecutando el código)

print('Creación de objetos' .center(50, '-'))
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrarDetalles()

    print(__name__)

print('Eliminación de Objetos'.center(50, '-'))
# todo se elimina al ejecutar la funcion (no es común usarlo)
del persona5
