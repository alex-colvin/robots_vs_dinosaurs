from robot import Robot
import random
class Fleet:
    
    def __init__(self, name) -> None:
        self.name - name
        self.robots = [Robot("Wall-E"), Robot("Eve"), Robot("Auto")]
        self.active_robot = None
        self.total_fleet_health = None
        self.living_robots = []

    def select_active_robot(self):
        self.calculate_living_robots()
        self.active_robot = random.choice(self.living_robots)

    def calculate_fleet_health(self):
        self.total_fleet_health = 0
        for robot in self.robots:
            self.total_fleet_health += robot.health
    
    def calculate_living_robots(self):
        self.living_robots.clear()
        for robot in self.robots:
            if robot.health > 0:
                self.living_robots += robot

