archivo = open('prueba.txt', 'r', encoding='utf8')  # r => read
"""

print(archivo.read())

# ----------------------------------------

archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(16))
# print(archivo.read(10)) # Continuamos desde la línea anterior
print(archivo.readline())
print(archivo.readline())



archivo = open('c:\\Users\\Rodrigo\\TecnicaturaGit\\Python2\\Archivos\\Leccion02\\prueba.txt', 'r', encoding='utf8')



# Vamos a iterar el archivo, cada una de las líneas
for linea in archivo:
    print(linea)  # iteramos todos los elementos del archivo

#  Accedemos al archivo como si fuera una lista
print(archivo.readlines())
print(archivo.readlines(3))
print(archivo.readlines()[11])

"""

# Anexamos información, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()  # cerramos el primer archivo
archivo2.close()  # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')