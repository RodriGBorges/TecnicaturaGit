#  La clase se carga en memoria
class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variableClase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variableInstancia = variable_instancia


print(MiClase.variableClase)

miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variableInstancia)
print(miClase1.variableClase)

print("")

miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variableInstancia)
print(miClase2.variableClase)