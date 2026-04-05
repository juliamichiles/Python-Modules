#!/usr/bin/python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plants(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


# ---------- DEMO ------------
def test_watering_system() -> None:

    bad_plants = ["Tomato", "lettuce"]
    good_plants = ["Tomato", "Lettuce", "Carrots"]

    print("=== Garden Watering System ===\n")

    # --- VALID PLANTS ---
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        for plant in good_plants:
            water_plants(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")

    # --- INVALID PLANTS ---
    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        for plant in bad_plants:
            water_plants(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
