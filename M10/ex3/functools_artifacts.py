#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    # Use functools.reduce to combine all spell powers
    
    operations = dict[str, Callable[[int, int], int]] = {
        # Support operations: "add", "multiply", "max", "min"
        # Use operator module functions (add, mul, etc.)
            "add": operator.add,
            "multiply": operator.mul,
            "max": max, # why using these without '()' here?
            "min": min
    }

    # If spells is empty, return 0
    if not spells:
        return 0
    
    # If operation is unknown, properly handle the error
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'")

    # Return the final reduced value
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    # Take a base enchantment function with signature:
    # (power: int, element: str, target: str) -> str

    lightning_enchanter = partial(base_enchantment, 50, "fire")
    fire_enchanter = partial(base_enchantment, 50, "ice")
    ice_enchanter = partial(base_enchantment, 50, "lightning")

    # Use functools.partial to create 3 specialized versions
    # Each version pre-filling power=50 and the element 
    return = {
            'lightning': lightning_enchanter,
            'fire': fire_enchanter,
            'ice': ice_enchanter
    }
    

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    # Use functools.lru_cache decorator for memoization
    # Implement fibonacci sequence calculation
    # Function should return the nth Fibonacci number
    # The cache should improve performance for repeated calls
    # Return the nth fibonacci number
    
    if n == 0:
        return 0

    if n == 1:
        return 1

    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
    

def spell_dispatcher() -> Callable[[Any], str]:
    # spell_dispatcher() - Create single dispatch system:
    # Use decorator functools.singledispatch to create a spell system
    # The base function receives Any and handles unknown spell type
    # Handle different types: int (damage spell), str (enchantment), list (multi-cast)
    # Return the dispatcher function
    # Each type should have appropriate spell behavior
    
    @singledispatch
    def call_spell(spell):
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell):
        return f"{spell} damage"

    @cast_spell.register(str)
    def _(spell):
        return spell

    @cast_spell.register(list)
    def _(spell):
        return f"{len(spells)} spells"

    return cast_spell

def main() -> None:
    #TODO: this

if __name__ == '__main__':
    main()
