import random

numerosAleatorios = []

for i in range(1, 21):
    numerosAleatorios.append(random.randint(1, 20))

numerosAleatorios.sort()
print(numerosAleatorios)

for number in numerosAleatorios:
    print("numero:", number, " cuadrado:", number ** 2, " cubo:", number ** 3)
