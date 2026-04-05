#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    temps = ["25", "abc", "100", "-50"]
    for temp in temps:
        print(f"\nInput data is '{temp}'")
        try:
            value = input_temperature(temp)
            print(f"Temperature is now {value}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
