from robot import Robot
from dinosaur import Dinosaur
class Battlefield:

    def __init__(self) -> None:
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("Spike", 25)
    
    def run_game (self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome (self):
        print("Welcome to Robots vs Dinosaurs, where to future battles with the past.")

    def battle_phase (self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
            else:    
                break
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
            else:
                break

    def display_winner (self):
        if self.dinosaur.health > 0:
            print(f"{self.dinosaur.name} has defeated {self.robot.name}.")
        else:
            print(f"{self.robot.name} has defeated {self.dinosaur.name}.")