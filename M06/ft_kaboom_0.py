#!/usr/bin/python3
from alchemy import grimoire


def ft_kaboom_0() -> None:

    ingredients = "Earth, wind and fire"
    spell_name = "fantasy"
    spell = grimoire.light_spell_record(spell_name, ingredients)

    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {spell}")


if __name__ == '__main__':
    ft_kaboom_0()
