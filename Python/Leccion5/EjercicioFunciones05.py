"""

 Ejercicio 05: Convertidor de temperaturas
 Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.
 Investigar las fórmulas

"""

def deCelsiusAFahrenheit(gradosC):
    return gradosC * 9 / 5 + 32 # La presedencia: multiplicación, división y suma

def deFahrenheitACelsius(gradosF):
    return (gradosF - 32) * 5 / 9 # La presedencia con parentesis: resta, multiplicación y división


celsius = float(input('Ingrese el valor de celsius: '))
resultado = deCelsiusAFahrenheit(celsius)
print(f'{celsius}°C --> {resultado:.2f}f')

# resultado:.2f para mostrar solo 2 dígitos después de la coma

fahrenheit = float(input('Ingrese el valor de fahrenheit: '))
resultado2 = deFahrenheitACelsius(fahrenheit)
print(f'{fahrenheit}f --> {resultado2:.2f}°C')