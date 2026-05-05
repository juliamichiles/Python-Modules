#!/usr/bin/python3
import alchemy


def ft_distillation_1() -> None:

    s_potion = alchemy.potions.strength_potion()
    h_potion = alchemy.heal()

    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {s_potion}")
    print(f"Testing heal alias: {h_potion}")


if __name__ == '__main__':
    ft_distillation_1()
