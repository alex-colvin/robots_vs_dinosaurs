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
    
    def select_campaign_robot(self):
        user_input=100
        max_robots = len(self.robots) - 1
        while user_input > max_robots:
            n = 0
            for robot in self.robots:
                print(f"{n} : {robot.name}")
                n += 1
            user_input = abs(int(input("Choose a robot by its number :")))
        print("You chose " + str(self.robots[user_input].name) + ".")
        self.active_robot = self.robots[user_input]
    
    def calculate_living_robots(self):
        for robot in self.robots:
            if robot.health == 0:
                self.robots.remove(robot)
                print(f"{robot.name} has been defeated.")

