#!/usr/bin/python3

def ft_kaboom_1() -> None:

    ingredients = "bats, frogs, arsenic, and eyeball"
    spell_name = "horrible curse"

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN EXCEPTION")

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        spell = dark_spell_record(spell_name, ingredients)

        print(f"Testing record dark spell: {spell}")

    except ImportError as e:
        print("... and I caught it because the subject sayed I could :)")
        print(f"Caught: {e}")


if __name__ == '__main__':
    ft_kaboom_1()
