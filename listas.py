listaCompras = ["Arveja", "Tamales", "Tomate", "Lechuga", "Naranjas"]
tuplaPrecios = (3.40, 31.0, 12.0, 11.0, 4.2)
conjunto = set([1, 3, 5])
conjunto2 = {11, 4, 3, 15, 2}
diccionario = {
    "c": "Tercera letra del abecedario",
    "a": "Primera letra del abecedario",
    "b": "Segunda letra del abecedario",
}

print(listaCompras)
print(tuplaPrecios)
print(conjunto)
print(conjunto2)
print(diccionario)

print(conjunto.intersection(conjunto2))
print(conjunto.union(conjunto2))

print(type(listaCompras))
print(type(tuplaPrecios))
print(type(conjunto))
print(type(conjunto2))
print(type(diccionario))

print(type(listaCompras[0]))

popped = conjunto.difference(conjunto2)
print(popped)
print(type(popped))

print(sorted(diccionario.values()))

"""Estructura de datos"""

"""Listas: Revertir el orden de los elementos de una lista"""

datosPersona = ["Luis", "Gutierrez", 39, "20/04/1981"]

datosPersona.reverse()

print("Los valores de mi nueva lista son:", datosPersona)