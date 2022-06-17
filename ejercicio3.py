diccionario = {}

diccionario["nombre"] = str(input("Ingresa el nombre: "))
diccionario["apellido"] = str(input("Ingresa el apellido: "))
diccionario["edad"] = int(input("Ingresa la edad: "))
diccionario["dni"] = str(input("Ingresa el dni: "))

print("Diccionario: ", diccionario)

listaFromDiccionario = list(diccionario)
print("Conversion de diccionario a lista:", listaFromDiccionario)
print("Tipo de datos de list(diccionario): ", type(listaFromDiccionario))

diccionario["profesion"] = str(input("Ingresa la profesion: "))

del diccionario["dni"]
print("Diccionario al final: ", diccionario)
