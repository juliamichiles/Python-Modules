#!/usr/bin/python3
import alchemy.transmutation.recipes


def ft_transmutation_0() -> None:

    gold = alchemy.transmutation.recipes.lead_to_gold()

    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {gold}")


if __name__ == '__main__':
    ft_transmutation_0()
