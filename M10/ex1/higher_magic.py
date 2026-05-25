#!/bin/usr/env python3
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    # Combine two spells:
    # Return a new function that calls both spells with the same arguments
    # The combined spell should return a tuple of both results
    # Example: combined = spell_combiner(fireball, heal)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    # Amplify spell power:
    # Returns a function with the same signature as the original spell
    # Returns a new spell where the power is multiplied before casting.
    # Example: mega_fireball = power_amplifier(fireball, 3)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    # Cast spell conditionally:
    # Returns a new spell that only casts if a condition is True
    # If condition fails, return "Spell fizzled"
    # Both condition and spell receive the same arguments


def spell_sequence(spells: list[Callable]) -> Callable:
    # Create spell sequence:
    # Return a function that casts all spells in order
    # Each spell receives the same arguments
    # Returns a list of all spell results


def main() -> None:
    # Your program must demonstrate use and efficiency of all your spells modifiers functions
