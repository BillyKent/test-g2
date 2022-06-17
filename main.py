cursos = {
    "curso1": "Bases de Datos",
    "curso2": "Estructuras de datos",
    "curso3": "Programacion",
    "curso4": "Algebra Lineal",
    "curso6": "Calidad de Software",
}
print("Diccionario inicial:", cursos)

print("Eliminando curso1")
del cursos["curso1"]

print("Diccionario ", cursos)

print("Comprobando existencia del curso \"Calidad de Software\":", "Calidad de Software" in cursos.values())

print("Agregando carrera \"Ingenieria de Software\"")
cursos["carrera"] = "Ingenieria de Software"

print("Diccionario final:", cursos)
