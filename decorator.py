def funcionA(funcionB):
    def funcionC():
        print("Inicio funcion C")
        funcionB()
        print("Fin funcion C")

    return funcionC


# @funcionA
def funcionB():
    print("Hola soy la funcion b")


funcionB()

# print(type(print("asdas")))

# funcionA(funcionB)()
