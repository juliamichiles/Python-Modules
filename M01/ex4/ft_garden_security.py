#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height=0, age=0):
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_age(self):
        return self._age


def ft_garden_security():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm [OK]")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days [OK]")
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
