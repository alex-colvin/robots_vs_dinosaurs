class Dinosaur:

    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack (self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacked {robot.name} causing {self.attack_power} damage.")
        
