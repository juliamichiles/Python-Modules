#!/usr/bin/python3

def check_temperature(temp_str: str) -> int | None:

    print(f"Testing temperature: {temp_str}")
    try:
        n: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    else:
        if n < 0:
            print(f"Error: {n}°C is too cold for plants (min 0°C)\n")
            return None
        elif n > 40:
            print(f"Error: {n}°C is too hot for plants (max 40°C)\n")
            return None
        else:
            print(f"Temperature {n}°C is perfect for plants!\n")
            return n

def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===\n")
    strings: list = [
            "25",
            "abc",
            "100",
            "-50",
        ]
    for string in strings:
       check_temperature(string) 
    
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
