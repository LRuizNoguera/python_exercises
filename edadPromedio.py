cantUsuarios = int(input("Por favor ingrese la cantidad de usuarios "))

edades = []

for i in range(cantUsuarios):
    edad = int(input(f"Ingrese la edad del empleado {i + 1} "))
    edades.append(edad)

def calcularPromedio(edades):
    sumaEdades = sum(edades)
    promedio = sumaEdades / len(edades)
    return promedio

promedioEdades = calcularPromedio(edades)

print(f"La edad promedio de los empleados es: {promedioEdades: .2f}")
