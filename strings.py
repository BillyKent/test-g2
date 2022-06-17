saludo = "Hola munda"
print(saludo)  # Hola munda

nuevoSaludo = saludo.replace("a", "e")
print(nuevoSaludo)  # Hole munde

# Sintaxis para slicing: string[<start_inclusive>:<end_exclusive>:<step>]
# Por defecto <start_inclusive> = 0
# Por defecto <end_exclusive> = longitud de la cadena
# Por defecto <step> = 1


cadena = "Hola mundo"
print(cadena[0:4])  # Hola
print(cadena[0:4:1])  # Hola
print(cadena[:])  # Hola mundo
print(cadena[::])  # Hola mundo
print(cadena[::2])  # Hl ud   (Cortando de dos en dos)
print(cadena[::-1])  # odnum aloH   (Invierte la cadena)

# Multiplicacion de strings
multiplicado = (cadena + ", ") * 4
print(multiplicado)  # Hola mundo, Hola mundo, Hola mundo, Hola mundo,

print(cadena.upper())  # HOLA MUNDO     (texto a mayuscula)
print(cadena.lower())  # hola mundo     (texto a minuscula)
print(cadena.title())  # Hola Mundo     (capitalizar primeras letras)
print(cadena.replace('a', 'e'))  # Hole mundo
print("    Mia Khalifa   ".lstrip())  # (Mia Khalifa   )  #Trim por la izquierda
print("    Mia Khalifa   ".rstrip())  # (    Mia Khalifa)  # Trim por la derecha
print("    Mia Khalifa   ".strip())  # (Mia Khalifa)  # Trim

print("base = 3".split())  # ['base', '=', '3']
print("base = 3".split("="))  # ['base ', ' 3']

formatted = "Hola, {} Bienvenido a {}".format('Billy', "Islandia")
print(formatted)  # Hola, Billy Bienvenido a Islandia

formattedNamed = "Hola {nombre} eres un {insulto}".format(nombre='Billy', insulto='mongol')
print(formattedNamed)  # Hola Billy eres un mongol

textoCompleto = "Este es un baile de mrd"
sujeto = textoCompleto.find("Este")
print(sujeto)  # 0
groseriaIndex = textoCompleto.find("mrd")
print(groseriaIndex)  # 20
noEncontradoIndex = textoCompleto.find("AEA")
print(noEncontradoIndex)  # -1
