import random

listaAleatoria = []
for i in range(10):
    listaAleatoria.append(random.randint(1, 10))
print("Lista aleatoria:", listaAleatoria)

listaCuadrados = []
listaCubos = []

for number in listaAleatoria:
    listaCuadrados.append(number ** 2)
    listaCubos.append(number ** 3)

print("Lista de cuadrados", listaCuadrados)
print("Lista de cubos", listaCubos)

listaInversa = listaCuadrados + listaCubos
listaInversa.reverse()
print("Suma de ambas listas de manera inversa:", listaInversa)
