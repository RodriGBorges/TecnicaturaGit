# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según que sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos

import random
numero = random.randint(0, 100)
print("Adivina el número")
numeroJugador = int(input("Ingrese un número: "))
intentos = 1
while numero != numeroJugador:
    if(numero > numeroJugador):
        print(f"Ingresaste {numeroJugador}, el número a adivinar ES MAYOR")
    else:
        print(f"Ingresaste {numeroJugador}, el número a adivinar ES MENOR")
    intentos += 1
    numeroJugador = int(input("\nIngrese otro número: "))
    print(f"Número de intentos: {intentos}")

print("\n¡¡Acertaste!!")
print(f"El número era: {numero}")
print(f"Número de intentos: {intentos}")

"""
print("\t.:Juego Adivina el número:.")
aleatorio = random.randint(0, 100)
contador = 0

while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif numero < aleatorio:
        print("\tNo es el número, digite un número mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
        break # rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")
"""