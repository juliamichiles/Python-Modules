#!/usr/bin/python3
import alchemy.transmutation


def ft_transmutation_1() -> None:

    gold = alchemy.transmutation.lead_to_gold()

    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {gold}")


if __name__ == '__main__':
    ft_transmutation_1()
