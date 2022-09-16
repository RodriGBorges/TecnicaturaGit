# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

n = int(input("Ingrese un número: "))

while n < 0: # Mientras el número sea negativo
    print("Error --> El número tiene que ser positivo")
    n = int(input("Ingrese un número: "))
factorial = 1 # La variable para calcular la factorial
for i in range(1, n+1):
    factorial *= i
print(f"\nEl factorial del número {n} positivo ingresado es: {factorial}")