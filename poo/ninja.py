class Ninja:
    # Numero total de ninjas
    num_ninjas = 0

    def __init__(self, name):
        self.name = name
        Ninja.num_ninjas += 1

    # S, A, B, C, D
    def set_current_mission(self, current_mission):
        self.current_mission = current_mission

    def get_current_mission(self):
        return self.current_mission

    def get_saludo(self):
        return "Hola, soy {}".format(self.name)

    def saludar(self):
        print(self.get_saludo())

    def alardear(self):
        print("Mi mision actual es de rango: {}".format(self.current_mission))

    def print_ninja_count(self):
        print("El numero de ninjas es ${}".format(Ninja.num_ninjas))


class Jounin(Ninja):
    def __init__(self, name, especialidad):
        self.name = name
        self.especialidad = especialidad
        Ninja.num_ninjas = -1

    def pelear(self):
        print("Soy un Jounin y estoy peleando")

    def get_especialidaad(self):
        return self.especialidad

    def __str__(self):
        return "Hola soy un Jounin, me llamo {} y mi especialidad es {}.".format(self.name, self.especialidad)


class Genin(Ninja):
    def __init__(self, name, sensei):
        super().__init__(name)
        self.sensei = sensei

    def pelear(self):
        print("Soy un Genin y estoy peleando con mi sensei", self.sensei.name)
