#!/usr/bin/python3

def check_plant_health(plant_name: str,
                       wtr_lvl: int,
                       sl_hr: int) -> None:

    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if wtr_lvl > 10:
        raise ValueError(f"Error: Water level {wtr_lvl} is too high (max 10)")
    if wtr_lvl < 1:
        raise ValueError(f"Error: Water level {wtr_lvl} is too low (min 1)")
    if sl_hr > 12:
        raise ValueError(f"Error: Sunlight hours {sl_hr} is too high (max 12)")
    if sl_hr < 2:
        raise ValueError(f"Error: Sunlight hours {sl_hr} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        message = check_plant_health("tomato", 6, 8)
        print(f"{message}")
    except ValueError as e:
        print(f"{e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 6, 8)
    except ValueError as e:
        print(f"{e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("carrot", 15, 8)
    except ValueError as e:
        print(f"{e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("beet", 6, 0)
    except ValueError as e:
        print(f"{e}")
    finally:
        print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
