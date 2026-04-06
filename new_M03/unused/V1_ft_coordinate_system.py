#!/usr/bin/python3
import sys
import math

# Aut: sys, sys.argv, math, math.sqrt(), tuple(), int(), float(), print(), split()

def ft_coordinate_system() -> None:

    print("=== Game Coordinate System ===\n")

    """ ====== PARSING ====== """

    coord_list = sys.argv[1].split(",")
    try:
        coord_tup = tuple(coord_list)
        x, y, z = coord_tup
        print(f"{x}, {y}, {z}")# remove
        x = int(x)
        y = int(y)
        z = int(z)
    
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
    
    """ ====== CALCULATING DISTANCE ====== """

    x1 = 0
    y1 = 0 
    z1 = 0
    distance  = math.sqrt((x-x1)**2 + (y-y1)**2 + (z-z1)**2)
    print(f"Parsed points: {coord_tup}")
    print(f"Distance between ({x1}, {y1}, {z1}) and {coord_tup}: {distance:.2f}")


if __name__ == "__main__":
    ft_coordinate_system()
