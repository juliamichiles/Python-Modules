#!/usr/bin/python3
from alchemy.elements import create_air


def ft_alembic_3() -> None:

    air = create_air()

    print("=== Alembic 3 ===")
    print(
            "Accessing alchemy/elements.py using "
            "'from ... import ...' structure"
    )
    print(f"Testing create_air: {air}\n")


if __name__ == '__main__':
    ft_alembic_3()
