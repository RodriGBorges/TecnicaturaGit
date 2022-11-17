"""
No es exactamente el mismo concepto de constantes en otros lenguajes de programación, sino que en python
simplemente es una convención (SIMULACIÓN), ya que realmente no existe el concepto de constantes en Python tal cual.
El concepto de constante tiene que ver para definir una variable y que no podamos modificar su valor, una
vez que le hemos asignado el valor a esta variable, ese concepto tal cual no existe en Python.

Asi que en Python a cualquier variable le podemos volver a asignar un valor.
Sin embargo, existe una convención para trabajar el concepto de constantes y poder simular este concepto
en Python.

El nombre de la variable debe ser en mayúsculas, esto es parte de la convención.
Así que una constante para poder identificarla, en primer lugar, definimos el nombre de la variable: MI_CONSTANTE

Se acostumbra a que estas variables se definan en un archivo / modulo por
separado y se utilicen por fuera de este módulo

"""

class Matematicas:
    PI = 3.1416 # Esta es una variable de clase constante


MI_CONSTANTE = 'Esta es una variable constante'
