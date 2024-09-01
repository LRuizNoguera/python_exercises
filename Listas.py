""" Se usan para almacenar diferentes tipos de datos pero con la diferencias que,
a éstas, sí se les pueden modificar sus elementos o agregar elementos nuevos.
Se definen en corchetes. """

lista1 = []
lista1.append("Aprendizaje automático") # Agregamos un elemento tipo string a la lista1
print(lista1)

lista2 = ["Python", "Java", "C++"]
print(lista2[0])

edades = [18, 22, 33, 15, 25, 26, 35, 40, 13, 20]
print("todas:", edades[:])
print("1-último:", edades[1:])
print("1-3:", edades[1:3])
print("0-penúltimo:", edades[0:-1])

# Len(lista): Permite obtener la longitud de una lista pasada como parámetro
# append(valor): Adiciona un nuevo valor a la lista
# insert(posición, valor): Permite agregar el elemento valor en la posición 'posición'
# del(elemento): Permite eliminar un elemento de la lista pasado como parámetro
# remove(elemento): Al igual que la anterior función, permite eliminar de la lista el elemento pasado como un parámetro
# sort([reverse=true]): Permite ordenar una lista en orden descendente



