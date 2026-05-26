#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    # Create a counting closure:
    # Return a function that counts how many times it’s been called
    # Each call should return the current count (starting from 1)
    # The counter should persist between calls
    # Creating two separate counters must yield independent state.

    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    #  Create power accumulator:
    # Return a function that accumulates power over time
    # Each call adds the given amount to the total power
    # Return the new total power after each addition
    # Start with initial_power as the base

    def add_power(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    #  Create enchantment functions:
    # Each factory creates functions with different enchantment types
    # Return a function that applies the specified enchantment

    def enchant_item(item_name: str) -> str:
        # Takes an item name and returns enchanted description
        # Format: "enchantment_type item_name" (e.g., "Flaming Sword")
        return enchantment_type + " " + item_name
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    # Create a memory management system:
    # Return a dict with ’store’ and ’recall’ functions
    # Use closure to maintain private memory storage

    vault = {}

    def store(key: Any, value: Any) -> None:
        # takes (key, value) and stores the memory
        # 'nonlocal' isn't needed here bc Python allows updating
        # the internal content of a dict natively, it is not the same
        # as reassigning the dict variable itself
        vault[key] = value

    def recall(key: Any) -> Any:
        # takes (key) and returns stored value or "Memory not found"
        if key in vault:
            return vault[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:

    # Memory Depths Test Data
    initial_powers = [69, 58, 57]
    power_additions = [9, 7, 6, 13, 19]
    enchantment_types = ['Earthen', 'Dark', 'Flowing', 'Light']
    items_to_enchant = ['Cloak', 'Ring', 'Amulet', 'Sword']

    magical_items = {
        "merlin_password": "Abracadabra_123!",
        "philosophers_stone_location": "Vault 713, Gringotts",
        "excalibur_status": "Resting in lake with Lady",
        "mana_potion_recipe": ["Nightshade", "Dragon Scale", "Moonlight Dew"],
        "elixir_count": 42,
        "forbidden_spell_id": 999,
        "is_dark_lord_defeated": True,
        "shadow_realm_coordinates": (51.5074, -0.1278),
    }

    # === Mage Counter ===
    print("\nTesting mage counter...\n")

    counter_a = mage_counter()
    counter_b = mage_counter()

    print("Created 'counter_a' and 'counter_b'")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"counter_b call 2: {counter_b()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_a call 4: {counter_a()}")
    print(f"counter_b call 3: {counter_b()}")

    # === Spell Accumulator ===

    print("\nTesting spell accumulator...\n")

    for base_power in initial_powers:

        ac = spell_accumulator(base_power)
        current_total = base_power
        print(f"Accumulator's Base Power: {base_power}")

        for add in power_additions:

            new_total = ac(add)
            print(
                    f"Power: {current_total} + added {add:2} "
                    f"-> Accumulated Total: {new_total}"
            )
            current_total = new_total

    # === Enchantment Factory ===
    print("\nTesting enchantment factory...\n")

    for i in range(4):
        factory = enchantment_factory(enchantment_types[i])
        print(factory(items_to_enchant[i]))

    # === Memory Vault ===
    print("\nTesting memory vault...\n")

    vault = memory_vault()

    print("Storing items in the memory vault...")

    for key, value in magical_items.items():
        vault["store"](key, value)
        # bc vault["store"] is a function in a dict and you can
        # access it through its key and call it all at once
        print(f"{key} was added to the vault")

    print("\nRecalling valid items from the vault...")

    for key in magical_items.keys():
        value = vault["recall"](key)
        print(f"Recall '{key}': {value}")

    print("\nRecalling invalid items from the vault...")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
    print(f"Recall 'invalid': {vault['recall']('invalid')}")


if __name__ == '__main__':
    main()
