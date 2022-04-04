from weapon import Weapon

class Robot:
    
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 30)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name} causing {self.active_weapon.attack_power} damage.")