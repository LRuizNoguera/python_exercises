""" Los diccionarios son una colección de datos mutables muy similar a las listas en cuanto a su función
de almacenamiento, pero con una diferencia en el modo de acceso a los elementos, realizado en este caso
por medio del uso de una clave, la cual debe expresarse entre corchetes y puede ser 'entero o cadena'.
A los diccionarios también se les conoce como arrays asociativos y se construyen empleando conjuntos de pares
clave - valor"""

registro = {"ID": 12345, "Nombre": "Carlos", "Apellido": "Pineda"}
print(registro)
print(registro["Nombre"])

registro["Profesión"] = "Profesor"
print(registro)
