#!/usr/bin/python3

class Error(Exception):
    pass

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise Error(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")

# ---------- DEMO ------------

def test_watering_system() -> None:

    bad_plants = ["tomato", None]
    good_plants = ["tomato", "lettuce", "carrots"]

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    try:
        water_plants(good_plants)
    except Error as e:
        print(f"Error: {e}")
    else:
        print("Watering completed successfully!\n")
    
    print("Testing with error...")
    try:
        water_plants(bad_plants)
    except Error as e:
        print(f"Error: {e}")
    else:
        print("Watering completed successfully!\n")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__": 
    test_watering_system() 
