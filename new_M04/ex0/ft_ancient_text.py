#!/usr/bin/python3
import sys


def ft_ancient_text() -> None:

    ac = len(sys.argv)
    if ac != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    file = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file}'")

    try:
        f = open(file, "r")
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print("File '{file}' closed.")
    except Exception as e:
        print(f"Error opening file '{file}': {e}\n")


if __name__ == "__main__":
    ft_ancient_text()
