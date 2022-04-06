from fleet import Fleet
from herd import Herd
import random
class Battlefield:

    def __init__(self) -> None:
        self.fleet = Fleet("BURN-E'S BOTS")
        self.herd = Herd("The Sharptooth Slayers")
        self.battle_royal_mode = True
    
    def run_game (self):
        self.display_welcome()
        if self.battle_royal_mode == True:
            self.battle_royale()
            self.display_winner()
        else:
            self.campaign_mode()

    def display_welcome (self):
        print("Welcome to Robots vs Dinosaurs, where to future battles with the past.")
        user_input = input("Would you like to play Battle Royal mode? Enter 'y', or Enter 'n' to play Campaign mode :")
        if user_input == 'n':
            self.battle_royal_mode = False


    def battle_royale (self):
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
    def campaign_mode (self):
        battle_level = 1
        self.fleet.select_campaign_robot()
        while self.fleet.active_robot.health > 0 and len(self.herd.dinosaurs) > battle_level:
            self.herd.select_campaign_dinosaur()
            print(f"Battle {battle_level} : {self.fleet.active_robot.name} VS {self.herd.active_dinosaur.name}")
            while self.fleet.active_robot.health > 0 and self.herd.active_dinosaur.health > 0:
                if self.fleet.active_robot.health > 0:
                    self.fleet.active_robot.attack(self.herd.active_dinosaur)
                else:
                    self.display_winner()
                    break
                if self.herd.active_dinosaur.health > 0:
                    self.herd.active_dinosaur.attack(self.fleet.active_robot)
                else:
                    self.fleet.active_robot.health = 100
                    self.display_winner()
                    battle_level += 1
                    break
        if self.fleet.active_robot.health > 0:
            print(f"CONGRATULATIONS {self.fleet.active_robot.name}!! You are the king of the Dinosaurs.")
        else:
            print("GAME OVER")
           
    def display_winner (self):
        if self.battle_royal_mode == True:
            if len(self.herd.dinosaurs) == 0:
                print(f"{self.fleet.name} have defeated {self.herd.name}.")
            else:
                print(f"{self.herd.name} have defeated {self.fleet.name}.")
        else:
            if self.fleet.active_robot.health == 0:
                print(f"{self.fleet.active_robot.name} was defeated by {self.herd.active_dinosaur.name}")
            else:
                print(f"{self.herd.active_dinosaur.name} was defeated by {self.fleet.active_robot.name}")
                