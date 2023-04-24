"""
try:
    10/0
except Exception as error:
    print(f'Ocurrió un error: {error}')

# -------------------------------------------

resultado = None
a = '10'
b = 0

try:
    resultado = a / b  # no sufre modificación por error
except ZeroDivisionError as error:  # Exception o ZeroDivisionError
    print(f'Ocurrió un error: {error}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# -------------------------------------------

resultado = None
a = 7
b = 5

try:
    resultado = a / b
except TypeError as error:
    print(f'TypeError - Ocurrió un error: {type(error)}')
except ZeroDivisionError as error:
    print(f'ZeroDivisionError - Ocurrió un error: {type(error)}')
except Exception as error:  # Clase padre más generica siempre al final
    print(f'Exception - Ocurrió un error: {type(error)}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# -------------------------------------------

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    resultado = a / b
except TypeError as error:
    print(f'TypeError - Ocurrió un error: {type(error)}')
except ZeroDivisionError as error:
    print(f'ZeroDivisionError - Ocurrió un error: {type(error)}')
except Exception as error:  # Clase padre más generica siempre al final
    print(f'Exception - Ocurrió un error: {type(error)}')

print(f'El resultado es: {resultado}')
print('seguimos...')

# -------------------------------------------

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    resultado = a / b
except TypeError as error:
    print(f'TypeError - Ocurrió un error: {type(error)}')
except ZeroDivisionError as error:
    print(f'ZeroDivisionError - Ocurrió un error: {type(error)}')
except Exception as error:  # Clase padre más generica siempre al final
    print(f'Exception - Ocurrió un error: {type(error)}')
else:
    print("No se arrojó ninguna excepción")
finally:  # Siempre se va a ejecutar
    print("Ejecución de este bloque finally")

print(f'El resultado es: {resultado}')
print('se sigue ejecutando el código...')

# -------------------------------------------
"""
from NumerosIgualesException import NumerosIgualesException
resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:  # raise => arroja una excepción
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b
except TypeError as error:
    print(f'TypeError - Ocurrió un error: {type(error)}')
except ZeroDivisionError as error:
    print(f'ZeroDivisionError - Ocurrió un error: {type(error)}')
except Exception as error:
    print(f'Exception - Ocurrió un error: {type(error)}')
else:
    print("No se arrojó ninguna excepción")
finally:
    print("Ejecución de este bloque finally")

print(f'El resultado es: {resultado}')
print('se sigue ejecutando el código...')