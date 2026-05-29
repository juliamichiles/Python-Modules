#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    # Use functools.reduce to combine all spell powers

    operations: dict[str, Callable[[int, int], int]] = {
        # Support operations: "add", "multiply", "max", "min"
        # Use operator module functions (add, mul, etc.)
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
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
    return {
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
    # Handle different types:
    # int (damage spell), str (enchantment), list (multi-cast)
    # Each type should have appropriate spell behavior

    # Use decorator functools.singledispatch to create a spell system
    @singledispatch
    def cast_spell(spell):
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell):
        return f"{spell} damage"

    @cast_spell.register(str)
    def _(spell):
        return spell

    @cast_spell.register(list)
    def _(spell):
        return f"{len(spell)} spells"

    # Return the dispatcher function
    return cast_spell


def main() -> None:

    # Ancient Library Test Data
    spell_powers = [17, 13, 35, 39, 41, 44]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [0, 1, 17, 13, 13, 25]

    print("\n==== Testing spell reducer ====\n")
    print(f"1) Testing with {spell_powers} and all valid operations")

    for op in operations:
        print(f"'{op.capitalize()}' operation:", end=" ")
        print(f"{spell_reducer(spell_powers, op)}")

    print("2) Testing with empty list and valid operation")
    print("'Add' operation:", end=" ")
    print(f"{spell_reducer([], 'add')}")

    print(f"3) Testing with {spell_powers} and unknown operation")
    print("'Power' operation:", end=" ")
    try:
        print(f"{spell_reducer(spell_powers, 'power')}")
    except ValueError as e:
        print(f"ValueError caught: {e}")

    print("\n=================================")
    print("=== Testing partial enchanter ===\n")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Casting {element} spell with power {power} on {target}!"

    b_enc = base_enchantment
    cast = partial_enchanter(b_enc)
    # this is a dict 'spell': partial_function

    print(f"1) Testing base enchantment:\n{b_enc(3, 'air', 'troll')}")

    print("2) Testing partial enchantments:")
    print(cast["fire"](target="goblin"))
    print(cast["ice"](target="goblin"))
    print(cast["lightning"](target="goblin"))

    print("3) Testing invalid key:")
    try:
        print(cast["water"](target="goblin"))
    except KeyError as e:
        print(f"KeyError caught: unknown key {e}")

    # this test gives a mypy error
    # print("4) Testing invalid base enchantment:")
    # try:
    #     print(partial_enchanter("string not a callable"))
    # except TypeError as e:
    #     print(f"TypeError caught: {e}")

    print("\n=================================")
    print("=== Testing memoized fibonacci ===\n")

    for n in fibonacci_tests:
        print(f"Fib({n}): ", memoized_fibonacci(n))
        print("Cache info:", memoized_fibonacci.cache_info())

    print("\n=================================")
    print("==== Testing spell dispatcher ====\n")

    disp = spell_dispatcher()

    print("Damage spell: ", disp(42))
    print("Enchantment: ", disp("fireball"))
    print("Multi-cast:", disp(spell_powers))
    print("Unknown spell type:", disp(42.42))


if __name__ == '__main__':
    main()
