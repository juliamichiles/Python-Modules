#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    def growing(self):
        self.height += 1
    def aging(self):
        self.age += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth():
    days = 7
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80,45),
        Plant("Cactus", 15, 120),
    ]
    initial_height = []
    for i in range(3):
        initial_height.append(plants[i].height)
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    print(f"=== Day {days} ===")
    for _ in range(days):
        for plant in plants:
            plant.growing()
            plant.aging()
    for plant in plants:
        print(plant.get_info())
    growth = plants[0].height - initial_height[0]
    print(f"Growth this week: +{growth}cm")

if __name__ == "__main__":
    ft_plant_growth()
