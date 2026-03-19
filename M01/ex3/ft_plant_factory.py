#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str = "Unknown",
                 height: int = 1, age: int = 1) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def grow_old(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    plants_info = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    plants = []
    print("=== Plant Factory Output ===")
    for i in range(6):
        if i < 5:
            plants.append(Plant(*plants_info[i]))
        else:
            plants.append(Plant())
        print(plants[i].get_info())
    i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    ft_plant_factory()
