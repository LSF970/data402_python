class Player_Character:
    Dragonborn = False
    HeroOfKvatch = False

    def __init__(self, name, race, gender, faction):
        self.name = name
        self.colour = race
        self.gender = gender
        self.faction = faction
    def DragonShout(self):
        if Player_Character.Dragonborn:
            return "Argh!"
        else:
            return "What? I don't know how to do that"

Luke = Player_Character("Luke", "Imperial", "Male", "Fighters Guild")
Maieeq = Player_Character("Maieeq", "Khajit", "Male", "No Faction")

print(Luke.Dragonborn)
print(Luke.DragonShout())
print(f"Character {Luke.name} belongs to {Luke.faction}")

print(Maieeq.Dragonborn)
print(Maieeq.DragonShout())
print(f"Character {Maieeq.name} belongs to {Maieeq.faction}")

