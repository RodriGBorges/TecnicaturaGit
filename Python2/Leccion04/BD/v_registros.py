import psycopg2

conexion = psycopg2.connect(user='postgres', password='root', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'  # Placeholder
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)


except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
