from dinosaur import Dinosaur
class Herd:
    def __init__(self, name) -> None:
        self.name = name
        self.dinosaurs = [Dinosaur("Littlefoot", 10), Dinosaur("Ducky", 15), Dinosaur("Chomper", 20)]