#!/usr/bin/python3
from alchemy.potions import strength_potion, healing_potion


def ft_distillation_0() -> None:

    s_potion = strength_potion()
    h_potion = healing_potion()
    
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {s_potion}")
    print(f"Testing healing_potion: {h_potion}\n")


if __name__ == '__main__': 
    ft_distillation_0()
