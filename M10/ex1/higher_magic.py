#!/usr/bin/env python3
from collections.abc import Callable
# collections.abc.Callable represents actual callable objects at runtime
# It integrates better with isinstance() and Python’s object model
# opposed to Typing's older-style static typing.


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    # Combine two spells:
    # Return a new function that calls both spells with the same arguments

    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be Callable")

    def spell_combo(target: str, power: int) -> tuple[str, str]:
        # The combined spell should return a tuple of both results

        result1 = spell1(target, power)
        result2 = spell2(target, power)

        return (result1, result2)

    return spell_combo


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    # Amplify spell power:
    # Returns a function with the same signature as the original spell

    if not callable(base_spell):
        raise TypeError("Spell must be Callable")

    def amplified_spell(target: str, power: int) -> str:
        # Returns a new spell where the power is multiplied before casting.

        amp_power = power * multiplier

        return base_spell(target, amp_power)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    # Cast spell conditionally:
    # Both condition and spell receive the same arguments
    if not callable(condition) or not callable(spell):
        raise TypeError("Both spell and condition must be Callable")

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            # Returns a new spell that only casts if a condition is True
            return spell(target, power)
        else:
            # If condition fails, return "Spell fizzled"
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    # Create spell sequence:
    # Return a function that casts all spells in order
    for spell in spells:
        if not callable(spell):
            raise TypeError("All spells must be Callable")

    def sequence_caster(target: str, power: int) -> list[str]:
        # Each spell receives the same arguments

        sequence = []
        for spell in spells:
            result = spell(target, power)
            sequence.append(result)

        # Returns a list of all spell results
        return sequence

    return sequence_caster


def main() -> None:

    # Test spells
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}! ({target}: -{power} damage!)"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power}HP"

    def turn_into_a_rat(target: str, power: int) -> str:
        return f"{target} was turned into a rat for {power} minutes!"

    def turn_rich(target: str, power: int) -> str:
        return f"{target} just got {power} times richer!"

    spell_list = [fireball, heal, turn_into_a_rat, turn_rich]

    # Test condition:
    def is_strong(target: str, power: int) -> bool:
        return power > 7

    t_vals = [6, 15, 9]
    t_targs = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # --- SPELL COMBINER ---
    print("\n=== Testing spell combiner... ===\n")
    try:
        combined = spell_combiner(fireball, heal)
        result = combined(t_targs[1], t_vals[0])

        print(f"Combined spell result:\n\t{result}")
    except TypeError as e:
        print(e)

    # --- POWER AMPLIFIER ---
    print("\n=== Testing power amplifier... ===\n")

    try:
        multiplier = 3
        original_power = 10
        amplified = power_amplifier(fireball, multiplier)

        print(
                f"Original: {original_power}, Amplified:"
                f"{original_power * multiplier}"
        )
        print(f"Original:\n\t{fireball(t_targs[2], t_vals[1])}")
        print(f"Amplified:\n\t{amplified(t_targs[2], t_vals[1])}")

    except TypeError as e:
        print(e)

    # --- CONDITIONAL CASTER ---
    print("\n=== Testing conditional caster... ===\n")

    try:
        cond_cast = conditional_caster(is_strong, fireball)
        above = cond_cast(t_targs[1], t_vals[1])
        below = cond_cast(t_targs[0], t_vals[0])

        print(f"Value above condition (power=15):\n\t{above}")
        print(f"Value below condition (power=6):\n\t{below}")
    except TypeError as e:
        print(e)

    # --- SPELL SEQUENCE ---
    print("\n=== Testing spell_sequence... ===\n")

    try:
        sequence = spell_sequence(spell_list)
        spells = sequence(t_targs[1], t_vals[2])

        for spell in spells:
            print(spell)

    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
