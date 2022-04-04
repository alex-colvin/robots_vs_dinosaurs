from fleet import Fleet
from herd import Herd
import random
class Battlefield:

    def __init__(self) -> None:
        self.fleet = Fleet("BURN-E'S BOTS")
        self.herd = Herd("The Sharptooth Slayers")
    
    def run_game (self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome (self):
        print("Welcome to Robots vs Dinosaurs, where to future battles with the past.")

    def battle_phase (self):
        while self.fleet.robots and self.herd.dinosaurs:
            self.fleet.select_active_robot()
            if len(self.fleet.robots) >= 1:
                self.fleet.active_robot.attack(random.choice(self.herd.dinosaurs))
            else:
                break
            self.herd.select_active_dionsaur()
            if len(self.herd.dinosaurs) >= 1:
                self.herd.active_dinosaur.attack(random.choice(self.fleet.robots))
            else:
                break
           
    def display_winner (self):
        if len(self.herd.dinosaurs) == 0:
            print(f"{self.herd.name} have defeated {self.fleet.name}.")
        else:
            print(f"{self.fleet.name} have defeated {self.herd.name}.")
