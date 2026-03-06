#!/usr/bin/python3

import sys


def ft_command_quest() -> None:

    print("=== Command Quest ===")

    count = len(sys.argv)
    if count == 1:
        print("No arguments provided!")

    else:
        print(f"Arguments received: {count - 1}")
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print(f"Argument {i}: {arg}")

    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {count}")


if __name__ == "__main__":
    ft_command_quest()
