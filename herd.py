from dinosaur import Dinosaur
import random
class Herd:
    def __init__(self, name) -> None:
        self.name = name
        self.dinosaurs = [Dinosaur("Littlefoot", 10), Dinosaur("Ducky", 15), Dinosaur("Chomper", 20)]
        self.active_dinosaur = None
        self.total_herd_health = None
        self.living_dinosaurs = []

    def select_active_dionsaur(self):
        self.active_dinosaur = random.choice(self.dinosaurs)
    
    def calculate_herd_health(self):
        self.total_herd_health = 0
        for dinosaur in self.dinosaurs:
            self.total_herd_health += dinosaur.health

    def calculate_living_dinosaurs(self):
        self.living_dinosaurs.clear()
        for dinosaur in self.dinosaurs:
            if dinosaur.health > 0:
                self.living_dinosaurs += dinosaur