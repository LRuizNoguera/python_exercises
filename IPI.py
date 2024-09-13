ingresosAnuales = float(input("Por favor ingrese el valor de sus ingresos anuales: "))

if ingresosAnuales < 85000000:
    impuesto = ingresosAnuales * 0.18 - 5560000
else:
    impuesto = 14000000 + (ingresosAnuales - 85000000) * 0.32

if impuesto < 0:
    print("El valos del impuesto a pagar es $0")
else:
 print("El valor del IPI a pagar es: ", impuesto)
