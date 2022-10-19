class Persona2:
    def __init__(self, nombre, apellido, edad):  # Está encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrarDetalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


# Comprobación del método principal en ejecución (de dónde se está ejecutando el código)
if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # LLamamos al método getter nombre

    persona1.nombre = 'Juan Pedro'  # LLamamos al método setter
    print(persona1.nombre)  # Otra vez con el método getter
    print(persona1.mostrarDetalles())  # LLamamos al método mostrarDetalles

    # Atributo read-only (solo lectura) seria la edad porque no tiene el método set (si lo borramos)
    print(persona1.edad)

    # Tarea crear tres objetos más, utilizando los métodos getter and setter
    # Para modificar, y mostrar los cambios con el método mostrar detalles

    persona2 = Persona2('Romi', 'Rome', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Romina'
    persona2.apellido = 'Soto'
    persona2.edad = 22
    print(persona2.mostrarDetalles())

    persona3 = Persona2('Fer', 'Garcia', 27)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Sarah'
    persona3.apellido = 'Connor'
    persona3.edad = 25
    print(persona3.mostrarDetalles())

    persona4 = Persona2('Luni', 'Mendez', 23)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Luna'
    persona4.apellido = 'Mendoza'
    persona4.edad = 26
    print(persona4.mostrarDetalles())

# Con este if evitamos llevar el código a otro archivo al importar
print(__name__)
