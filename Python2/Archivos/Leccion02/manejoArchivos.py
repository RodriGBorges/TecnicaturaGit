# Declaramos una variable

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # w => write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución, y producción\n')
    archivo.write('Las letras son:\nr > read - leer, \na > append - anexa, \nw > write - escribe, \nx > crea un archivo')
    archivo.write('\nt > esta es para texto o text, \nb > archivos binarios, \nw+ > lee y escribe son iguales r+\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos ')
except Exception as error:
    print(error)
finally:
    archivo.close()  # Con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto')  #El archivo ya se cerró
