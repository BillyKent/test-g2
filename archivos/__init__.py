def leerArchivo():
    archivoPrueba = open("prueba.txt", "r")
    print(archivoPrueba.read())


leerArchivo()

archivoPrueba = open("prueba.txt", "w")
archivoPrueba.write("Jejeje")

leerArchivo()


archivoPrueba = open("prueba.txt", "a+")
archivoPrueba.writelines(["Comer", "Reir", "Bailar", "Jugar"])

leerArchivo()