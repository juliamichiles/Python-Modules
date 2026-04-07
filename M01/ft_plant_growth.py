#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growing(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_plant_growth() -> None:
    days = 6
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),  # comment to print rose only
        Plant("Cactus", 15, 120),  # comment to print rose only
    ]
    initial_height = []
    rng = 3  # change back to 1 to print rose only
    for i in range(rng):
        initial_height.append(plants[i].height)
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    print(f"=== Day {days + 1} ===")
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
