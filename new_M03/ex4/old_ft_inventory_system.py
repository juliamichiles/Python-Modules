#!/usr/bin/python3
import sys


def print_sorted(items: dict, total: int) -> None:
    temp = dict()
    temp.update(items)

    print("\n=== Current Inventory ===")
    while len(temp) > 0:
        max_key = None
        max_value = -1

        for key, value in temp.items():
            if max_key is None or value > max_value:
                max_key = key
                max_value = value

        percent = max_value / total * 100
        unit = "unit" if max_value == 1 else "units"
        print(f"{max_key}: {max_value} {unit} ({percent:.1f}%)")

        new_temp = dict()
        for key, value in temp.items():
            if key != max_key:
                new_temp.update({key: value})
        temp = new_temp


def print_format(category: str, items: dict, count: int, b: bool) -> None:

    print(f"{category}:", end=" ")

    i = 0
    if b is True:
        for key in items.keys():
            i += 1
            if i < count:
                print(f"{key}, ", end="")
            else:
                print(key)
    else:
        for value in items.values():
            i += 1
            if i < count:
                print(f"{value}, ", end="")
            else:
                print(value)


def ft_inventory_system() -> None:

    items = sys.argv[1:]
    inventory = dict()
    item_types = len(items)

    print("=== Inventory System Analysis ===")
    for item in items:
        name, qty = item.split(":")
        inventory.update({name: int(qty)})

    total = 0
    scarce = dict()
    moderate = dict()
    restock = dict()

    for key, value in inventory.items():
        total += value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {item_types}")
    print_sorted(inventory, total)
    for key, value in inventory.items():
        if value < 4:
            scarce.update({key: value})
        elif value < 6:
            moderate.update({key: value})
        if value == 1:
            restock.update({key: value})

    print("\n=== Inventory Statistics ===")
    least_value = -1
    least_key = None

    most_value = -1
    most_key = None

    for key, value in inventory.items():

        if most_key is None or value > most_value:
            most_value = value
            most_key = key

        if least_key is None or value < least_value:
            least_value = value
            least_key = key

    unit = "unit" if most_value == 1 else "units"
    print(f"Most abundant: {most_key} ({most_value} {unit})")
    unit = "unit" if least_value == 1 else "units"
    print(f"Least abundant: {least_key} ({least_value} {unit})")

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    print_format("Restock needed", restock, len(restock), True)

    print("\n=== Dictionary Properties Demo ===")
    print_format("Dictionary keys", inventory, len(inventory), True)
    print_format("Dictionary values", inventory, len(inventory), False)
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
