from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as catalogo

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar película')
        print('2. Listar las películas')
        print('3. Eliminar catálogo de películas')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_peliculas(pelicula)
        elif opcion == 2:
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_peliculas()
    except Exception as error:
        print(f'Ocurrió un error de tipo: {error}')
        opcion = None
    else:
        print('Salimos del programa')