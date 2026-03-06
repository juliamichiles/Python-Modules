#!/usr/bin/python3
import math


# ---------------------------
# Distance Calculation
# ---------------------------
def calculate_distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance


# ---------------------------
# Coordinate Parsing
# ---------------------------
def parse_coordinates(coord_str: str) -> tuple:

    parts = coord_str.split(",")
    x, y, z = parts  # unpacks list into 3 strings
    return (int(x), int(y), int(z))


# ---------------------------
# Main Program
# ---------------------------
def ft_coordinate_system() -> None:

    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)

    # Create a position manually
    try:
        position = (10, 20, 5)
        dist = calculate_distance(origin, position)
        print(f"\nPosition created: {position}")
        print(f"Distance between {origin} and {position}: {dist:.2f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")

    # Parse valid coordinates string
    print("\nParsing coordinates: \"3,4,0\"")
    try:
        parsed_position = parse_coordinates("3,4,0")
        print(f"Parsed position: {parsed_position}")
        dist = calculate_distance(origin, parsed_position)
        print(f"Distance between {origin} and {parsed_position}: {dist:.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")

    # Parse invalid coordinates string
    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")

    # Demonstrate tuple unpacking
    x, y, z = parsed_position
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
