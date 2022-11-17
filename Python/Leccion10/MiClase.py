#  La clase se carga en memoria
class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variableClase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variableInstancia = variable_instancia

    @staticmethod
    def metodo_estatico(): # Método estático, se asocia a la clase
        print(MiClase.variableClase)

    @classmethod
    def metodo_clase(cls): # cls => es una referencia a la clase(se puede cambiar)
        print(cls.variableClase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variableClase)
        print(self.variableInstancia)

print(MiClase.variableClase)

miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variableInstancia)
print(miClase1.variableClase)

print("")

miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variableInstancia)
print(miClase2.variableClase)

print("")

MiClase.variableClase2 = 'Valor de variable de clase 2'
print(MiClase.variableClase2)
print(miClase1.variableClase2)
print(miClase2.variableClase2)

print("")
MiClase.metodo_estatico()

MiClase.metodo_clase()

miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()