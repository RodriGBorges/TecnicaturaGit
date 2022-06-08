# Ejercicio Etapas de vida según edad

edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:  #Sintaxis simplificada
    mensaje = 'La infancia es increíble y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 40 <= edad < 50:
    mensaje = 'El hogar y la familia es un cálido refugio'
elif 60 <= edad < 70:
    mensaje = 'No hay que quedarse solo con lo aprendido antes'
elif 80 <= edad < 90:
    mensaje = 'Mucho tiempo libre: Para compartir, dedicarse a uno mismo y jugar con los nietos'
elif 90 <= edad < 100:
    mensaje = 'Algunas cosas que solíamos hacer solos ya no podemos hacerlas, no está mal pedir ayuda'
else:
    mensaje = 'Error, no hay mensaje para esa edad'
print(f'tu edad es: {edad}, {mensaje}')