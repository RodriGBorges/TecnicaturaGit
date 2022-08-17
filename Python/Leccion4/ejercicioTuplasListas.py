# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]

nuevaListaTupla = []
for tupl in tupla:
    if(tupl < 5):
        nuevaListaTupla.append(tupl)
        print(f'Se agrega {tupl}')
    else:
        print(f'El número {tupl} no cumple con la condición')

print(f'Se terminaron de filtrar los números, la nueva lista contiene: ')
print(nuevaListaTupla)