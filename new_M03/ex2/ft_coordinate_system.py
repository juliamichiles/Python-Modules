#!/usr/bin/python3
import math


def pytof(num: str) -> float:

    frac = 0.0
    divisor = 1
    seen_dot = False
    digits = "0123456789"
    n = 0.0

    for c in num:
        i = 0
        found = False
        if c == '.':
            if seen_dot:
                raise ValueError(f"could not convert string to float: '{num}'")
            seen_dot = True
            continue

        for d in digits:
            if c == d:
                found = True
                break
            i += 1
        if not found:
            raise ValueError(f"could not convert string to float: '{num}'")

        if not seen_dot:
            n = n * 10 + i

        else:
            divisor *= 10
            frac = frac + i / divisor

    return n + frac


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
def get_player_pos() -> tuple:

    while True:
        user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = user_input.split(",")
        i = 0
        for part in parts:
            i += 1
        if i != 3:
            print("Invalid syntax")
            continue

        try:
            part_x = parts[0].strip()
            part_y = parts[1].strip()
            part_z = parts[2].strip()
            x = round(pytof(part_x), 2)
            y = round(pytof(part_y), 2)
            z = round(pytof(part_z), 2)
            return (x, y, z)

        except ValueError as e:
            for part in parts:
                try:
                    pytof(part)
                except ValueError:
                    print(f"Error on parameter '{part}': {e}")
                    break


# ---------------------------
# Main Program
# ---------------------------
def ft_coordinate_system() -> None:

    print("\n=== Game Coordinate System ===")

    origin = (0, 0, 0)

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = calculate_distance(origin, pos1)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = calculate_distance(pos1, pos2)
    print(
            "Distance between the 2 sets of coordinates: "
            f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    ft_coordinate_system()
