dicc = {}

dicc["hola"] = "Munda"
dicc["hello"] = "Moto"
dicc["hi"] = "Five"
dicc["tumor"] = "Cancer"

print(dicc)
del dicc["tumor"]
print(dicc)

listaOrdenadaKeys = sorted(dicc)
print(listaOrdenadaKeys)
print(sorted(dicc.values()))

lista = list(dicc)
print(lista)

print("-------------")
miDiccionario = {"nombre": "Amazon Web Services", "tipo": "cloud"}
print(miDiccionario)
print(list(miDiccionario))

valores = list(miDiccionario.values())
print("cloud" in valores)

listaADiccionario = ("nombre", "Billy", "apellido", "Macaco")
print(listaADiccionario)
diccionarioFromLista = dict([("nombre", "Billy")])
print(diccionarioFromLista)

lista1 = ["Margarita"]
lista2 = ["Mejía"]
lista3 = [20]

usuaario = lista1 + lista2 + lista3

print(usuaario)

print("---------------")

customDict = dict([("nombre", "Billy"), ("apellido", "Macaco"), ("edad", 23)])
print(customDict)
print(type(("nombre", "Billy")))

print(list(customDict.values()))
print(type(customDict.values()))
print(type(list(customDict.values())))
print(list(customDict))
print(sorted(customDict))
