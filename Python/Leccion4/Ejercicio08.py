# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones:
#                       1. Ingresar dinero en la cuenta
#                       2. Retirar dinero en la cuenta
#                       3. Mostrar dinero disponible
#                       4. Salir

saldo = 1000
print("Bienvenido al cajero autómatico RAPICASH5000")
while True:
    print("\t.:MENÚ:.")
    print("\t1. Ingresar dinero en la cuenta")
    print("\t2. Retirar dinero en la cuenta")
    print("\t3. Mostrar dinero disponible")
    print("\t4. Salir")
    opcion = int(input("Ingrese una opción de menú: "))
    print("")
    if opcion == 1:
        suma = float(input("Cuanto dinero desea ingresar --> "))
        saldo += suma
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 2:
        sacar = float(input("Cuanto dinero desea retirar --> "))
        if sacar > saldo:
            print()
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= sacar
            print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar el cajero RAPICASH5000")
        break
    else:
        print("ERROR --> esa opción no existe.")
        print()