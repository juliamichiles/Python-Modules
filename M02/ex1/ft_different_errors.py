#!/usr/bin/python3

def garden_operations() -> None:

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open('missing.txt')
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    test_dict = {"plant": "rose", "age": 25}
    try:
        test_dict["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    try:
        int("abc") / 0
    except(ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__": 
    test_error_types()
