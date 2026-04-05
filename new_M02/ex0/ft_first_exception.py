#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:

    print("=== Garden Temperature ===")

    strings: list = [
            "25",
            "abc",
        ]
    for string in strings:
        print(f"\nInput data is '{string}'")
        try:
            value = input_temperature(string)
            print(f"Temperature is now {value}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
