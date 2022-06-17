import ninja

kakashi = ninja.Ninja("Kakashi")
print(kakashi.name)

print(kakashi.get_saludo())
kakashi.saludar()

kakashi.set_current_mission("A")
print(kakashi.current_mission)
kakashi.alardear()

kakashi.print_ninja_count()
# ==========================

hayate = ninja.Jounin("Hayate Gekko", "Katana")
ibiki = ninja.Jounin("Ibiki Moreno", "Interrogacion")
asuma = ninja.Jounin("Asuma Sarutobi", "Viento")

print(hayate)
print(ibiki)

naruto = ninja.Genin("Naruto", hayate)
shikamaru = ninja.Genin("Shikamaru", asuma)
chouji = ninja.Genin("Chouji", asuma)

ninjas = (hayate, ibiki, asuma, naruto, shikamaru, chouji)
for ninja in ninjas:
    ninja.pelear()
