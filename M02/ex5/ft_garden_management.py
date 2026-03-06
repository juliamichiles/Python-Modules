#!/usr/bin/python3

""" ============= ERRORS ============= """


class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_name: str):
        message = f"The {plant_name} is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


""" ============= GARDEN MANAGER ============= """


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 5

    def tank_capacity(self) -> None:
        if self.water_tank < 2:
            raise WaterError("Not enough water in tank")
        elif self.water_tank > 10:
            raise WaterError(f"Water level {self.water_tank}"
                             f" is too high (max 10)")

    def check_health(self) -> None:
        for name, data in self.plants.items():
            try:
                sun = data["sun"]
                water = data["water"]
                if water < 2:
                    raise PlantError(name)
                if water > 10:
                    raise WaterError(f"Water level {water}"
                                     f" is too high (max 10)")
                if sun < 2 or sun > 10:
                    raise GardenError("Unhealty sunlight level")
                print(f"{name}: healthy (water: {water}, sun: {data['sun']})")
            except GardenError as e:
                print(f"Error checking {name}: {e}")

    def add_plant(self, name: str, water: int, sun: int) -> str:
        if not name:
            raise GardenError("Plant name cannot be empty!")
        self.plants[name] = {"water": water, "sun": sun}
        return f"Added {name} successfully"

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            self.tank_capacity()

            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")
    # methods to add plants, water plants, and check plant health


def test_garden_management() -> None:
    # Integration of all error handling techniques learned
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    # Adding plants with both valid and invalid inputs
    print("Adding plants to garden...")
    try:
        print(manager.add_plant("tomato", 5, 8))
    except GardenError as e:
        print(f"Error adding plant: {e}")
    try:
        print(manager.add_plant("lettuce", 7, 15))
    except GardenError as e:
        print(f"Error adding plant: {e}")
    try:
        print(manager.add_plant("", 5, 5))
    except GardenError as e:
        print(f"Error adding plant: {e}")

    # Watering plants with proper cleanup (using finally)
    print("\nWatering plants...")
    manager.water_plants()

    # Checking plant health and handling validation errors
    print("\nChecking plant health...")
    manager.check_health()
    # Error recovery = showing the system continues working after errors
    print("\nTesting error recovery...")
    manager.water_tank = 1
    try:
        manager.tank_capacity()
    except WaterError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
