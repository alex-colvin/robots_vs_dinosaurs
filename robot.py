from weapon import Weapon

class Robot:
    
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 30)

    def attack(self, dinosaur):
        if dinosaur.health >= self.active_weapon.attack_power:
            dinosaur.health -= self.active_weapon.attack_power
        else:
            dinosaur.health = 0
        print(f"{self.name} attacked {dinosaur.name} causing {self.active_weapon.attack_power} damage. {dinosaur.name} has {dinosaur.health} remaining.")

