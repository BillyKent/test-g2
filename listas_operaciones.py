enteros = [5, 2, 1, 3, 6, 4, 8, 9, 7]
print(enteros)
enteros.append(10)
print(enteros)
popped = enteros.pop(4)
print(popped)
print(enteros)
enteros.insert(4, popped)
print(enteros)
enteros.remove(6)
print(enteros)
print(enteros.count(10))

enteros.sort()
print(enteros)
copied = enteros.copy()
copied.reverse()
print("copied:", copied)

enteros.pop()
print(enteros)

del enteros[len(enteros) - 1]
print(enteros)

enteros.clear()
print(enteros)
