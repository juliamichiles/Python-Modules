#!/usr/bin/python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str):
        message = f"The {plant_name} is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


# ------------ Errors ---------------
def tank_capacity(water: int) -> None:
    if water < 2:
        raise WaterError("Not enough water in the tank")
    elif water > 90:
        raise WaterError("Tank is about to overflow")


def wilting(is_healthy: bool, plant_name: str) -> None:
    if not is_healthy:
        raise PlantError(plant_name)


# ------------ Demo ---------------
def errors_demo() -> None:

    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        wilting(False, "tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        tank_capacity(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        wilting(False, "tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        tank_capacity(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    errors_demo()
