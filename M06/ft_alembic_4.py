#!/usr/bin/python3
import alchemy


def ft_alembic_4() -> None:

    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print(f"This will raise an exception!")
    print("Testing the hidden create_earth:")
    try:
        print(f"{alchemy.create_earth()}\n")
    except AttributeError as e:
        print(f"Caught AttributeError: {e}\n")

if __name__ == '__main__':
    ft_alembic_4()
