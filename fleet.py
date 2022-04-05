from robot import Robot
import random
class Fleet:
    
    def __init__(self, name) -> None:
        self.name = name
        self.robots = [Robot("Wall-E"), Robot("Eve"), Robot("Auto")]
        self.active_robot = None
        self.living_robots = []

    def select_active_robot(self):
        self.calculate_living_robots()
        if len(self.robots) >= 1:
            self.active_robot = random.choice(self.robots)
            print(f"{self.active_robot.name} is ready to attack.")
    
    def calculate_living_robots(self):
        for robot in self.robots:
            if robot.health == 0:
                self.robots.remove(robot)
                print(f"{robot.name} has been defeated.")

