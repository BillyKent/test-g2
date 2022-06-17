persona1 = {}
persona2 = {}

persona1["nombre"] = input("Ingrese el nombre de la primera persona: ")
persona1["edad"] = input("Ingrese la edad de la primera persona: ")

persona2["nombre"] = input("Ingrese el nombre de la segunda persona: ")
persona2["edad"] = input("Ingrese la edad de la segunda persona: ")

print("Para el primer nombre ingresaste un dato de tipo ", type(persona1["nombre"]))
print("Para la primera edad ingresaste un dato de tipo ", type(persona1["edad"]))

print("Para el segundo nombre ingresaste un dato de tipo ", type(persona2["nombre"]))
print("Para la segunda edad ingresaste un dato de tipo ", type(persona2["edad"]))

edad1 = persona1["edad"]
edad2 = persona2["edad"]

print("Valores registrados para la persona 1:", persona1)
print("Valores registrados para la persona 2:", persona2)

if edad1.isnumeric() and edad2.isnumeric():
    print("La suma de ambas edades es: ", int(edad1) + int(edad2))
else:
    print("Ingresaste valores incorrectos...")
