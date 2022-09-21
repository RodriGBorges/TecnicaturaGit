"""
 Ejercicio 10: No repetir caracteres
 Hacer un programa que pida una cadena por consola, luego meter los caracteres en una lista sin repetir caracteres

"""

cadena = input("Ingrese una frase: ")
lista = []

for i in cadena:
    if(i not in lista):
        lista.append(i)

cadena = lista
print(f"\nLista de caracteres sin repetir ninguno: {cadena}")
