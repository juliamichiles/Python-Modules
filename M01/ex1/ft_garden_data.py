#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        print("{}: {}cm, {} days old".format(
            plants[i].name, plants[i].height, plants[i].age))


if __name__ == "__main__":
    ft_garden_data()
