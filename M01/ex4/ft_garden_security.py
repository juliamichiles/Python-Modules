#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print("\nInvalid operation attempted: "
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def get_height(self) -> None:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age

    def get_age(self) -> None:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    print(f"Height updated: {plant.get_height()}cm [OK]")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days [OK]")
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.name} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
