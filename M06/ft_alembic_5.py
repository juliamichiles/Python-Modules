#!/usr/bin/python3
from alchemy import create_air


def ft_alembic_5() -> None:

    air = create_air()

    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {air}\n")


if __name__ == '__main__':
    ft_alembic_5()
