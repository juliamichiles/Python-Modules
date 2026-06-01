#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
import time as t


def spell_timer(func: Callable) -> Callable:
    #  Create a decorator that measures function execution time
    #  Use functools.wraps to preserve original function metadata

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Print "Casting function_name..." before execution
        print(f"Casting {func.__name__}...")

        start = t.time()
        result = func(*args, **kwargs)
        end = t.time()

        # Print "Spell completed in X.XXX seconds" after execution
        print(f"Spell completed in {(end - start):.3f} seconds")

        # Return the original function’s result
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    #  Create a decorator factory that validates power levels

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[-1])
            if power >= min_power:
                # If power is valid, execute the function normally
                return func(*args, **kwargs)
            else:
                # If invalid, return "Insufficient power for this spell"
                return "Insufficient power for this spell"
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    #  Create a decorator that retries failed spells

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):

            # If function raises an exception, retry up to max_attempts times
            for attempt in range(1, max_attempts+1):
                try:
                    # If one attempt succeeds, return its result normally
                    return func(*args, **kwargs)
                except Exception:
                    print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                    )
            # If all attempts fail, return:
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        # Static method that checks if name is valid
        # (at least 3 characters and contains only letters/spaces)
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    # Master's Tower Test Data

    test_powers = [8, 14, 13, 7]
    spell_names = ['darkness', 'lightning', 'tornado', 'flash']
    mage_names = ['Casey', 'River', 'Luna', 'Riley', 'Nova', 'Alex']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    guild = MageGuild()

    @spell_timer
    def fire_ball() -> str:
        t.sleep(0.5)
        return "Fireball cast!"

    @retry_spell(4)
    def unstable_spell(n: int) -> str:
        if n > 5:
            return "Waaaaaaagh spelled!"
        else:
            raise Exception("Spell unstable")

    print("\n=== Testing spell timer ===")
    print(f"Result: {fire_ball()}\n")

    print("=== Testing retrying spell ===")
    print(f"{unstable_spell(4)}")
    print(f"{unstable_spell(6)}")

    print("\n=== Testing MageGuild ===")
    print("\n* Validating mage names... *")

    for name in mage_names:
        print(f"{name}: {MageGuild.validate_mage_name(name)}")

    for name in invalid_names:
        print(f"{name}: {MageGuild.validate_mage_name(name)}")

    print("\n* Attempting to cast spells... *")

    for i in range(4):
        spell = spell_names[i]
        power = test_powers[i]
        print(f"Testing spell '{spell}' with power {power}:")
        print(f"\t{guild.cast_spell(spell, power)}")


if __name__ == '__main__':
    main()
