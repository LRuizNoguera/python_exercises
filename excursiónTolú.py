gordos = int(input("Ingrese el número de gordos: "))
flacos = int(input("Ingrese el número de flacos: "))

puestos = gordos * 2 + flacos
bus = puestos // 50
comidaGordos = 4 * 4 * 3000 * gordos
comidaFlacos = 4 * 2 * 3000 * flacos

if puestos % 50 == 0:
    print("El número de buses es: ", bus)
else:
    bus = bus + 1
    print("El número de buses es: ", bus)

if puestos <= 200:
    valorBus = bus * 50000
else:
    valorBus = bus * 80000

print("El costo total de los buses es : ", valorBus)
print("El costo total de la comida es: ", comidaFlacos + comidaGordos)
print("El costo total de la excursión es: ", comidaFlacos + comidaGordos + valorBus)
