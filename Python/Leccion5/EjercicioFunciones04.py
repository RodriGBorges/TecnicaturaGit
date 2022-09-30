"""

 Ejercicio 04 : Calculadora de impuestos
 Crear una función para calcular el total de un pago incluyendo el impuesto aplicado (IVA)
 Formula: pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
 Proporcione el pago sin impuesto: 1000
 Proporcione el monto del impuesto: 21%
 Pago con impuesto: xxxxx

"""

def calcImpuesto(pagoSinImpuesto, impuesto):
    pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal


pagoSinImpuesto = float(input('Ingrese el pago sin impuestos: '))
impuesto = int(input('Ingrese el impuesto a aplicar: '))

pagoConImpuesto = calcImpuesto(pagoSinImpuesto, impuesto)

print(f'Pago con impuesto: {pagoConImpuesto}')