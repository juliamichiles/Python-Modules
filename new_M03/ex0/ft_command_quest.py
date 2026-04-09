#!/usr/bin/python3
import sys


def ft_command_quest() -> None:

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    count = len(sys.argv[0:])
    if count == 1:
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {count - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {count}\n")


if __name__ == "__main__":
    ft_command_quest()
