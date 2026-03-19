#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (
            f"{self.name} ({self.__class__.__name__}):"
            f"{self.height}cm, {self.age} days"
        )


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.color} color"


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def get_nutri(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.harvest_season} harvest"


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade = self.trunk_diameter * 2
        return f"{self.name} provides {shade} square meters of shade"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, {self.trunk_diameter}cm trunk diameter"


def ft_plant_types() -> None:
    flowers_info = [
        ("Rose", 25, 30, "Red"),
        ("Sunflower", 80, 45, "Yellow"),
    ]
    veggies_info = [
        ("Tomato", 80, 90, "Summer", "Vitamin C"),
        ("Carrot", 40, 80, "Spring", "Vitamin D"),
    ]
    trees_info = [
        ("Oak", 500, 1825, 50),
        ("Palm", 3000, 18250, 40),
    ]
    flowers = []
    veggies = []
    trees = []
    print("=== Garden Plant Types ===")
    for i in range(2):
        flowers.append(Flower(*flowers_info[i]))
        veggies.append(Vegetable(*veggies_info[i]))
        trees.append(Tree(*trees_info[i]))
        print(f"{flowers[i].get_info()}")
        print(f"{flowers[i].bloom()}\n")
        print(f"{veggies[i].get_info()}")
        print(f"{veggies[i].get_nutri()}\n")
        print(f"{trees[i].get_info()}")
        print(f"{trees[i].produce_shade()}\n")


if __name__ == "__main__":
    ft_plant_types()
