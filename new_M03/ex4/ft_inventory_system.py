#!/usr/bin/env python3
import sys


def pytoi(nb: str) -> int:

    digits = "0123456789"
    n = 0
    sign = 1
    num = nb

    if num[0] == '-':
        sign = -1
        num = nb[1:]
    elif num[0] == '+':
        num = nb[1:]

    for c in num:
        i = 0
        found = False
        for d in digits:
            if c == d:
                found = True
                break
            i += 1
        if not found:
            raise ValueError(f"could not convert string to int: '{nb}'")
        n = n * 10 + i

    return n * sign


def parse_inventory(args: list) -> tuple:
    inventory = {}
    order = []

    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty_str = parts

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = pytoi(qty_str)
        except Exception as e:
            print(f"Quantity error for '{name}': {e}")
            continue

        inventory[name] = qty
        order.append(name)

    return inventory, order


def print_inventory_analysis(inventory: dict, order: list) -> None:
    print("=== Inventory System Analysis ===")
    print(f"Got inventory: {inventory}")

    total = sum(inventory.values())
    items = list(inventory.keys())

    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total}")

    # Percentages
    for item in order:
        percent = (inventory[item] / total) * 100
        print(f"Item {item} represents {round(percent, 1)}%")

    if total > 0:
        # Percentages
        for item in order:
            percent = (inventory[item] / total) * 100
            print(f"Item {item} represents {round(percent, 1)}%")

        # Most & least abundant
        max_item = None
        min_item = None
        for item in order:
            if max_item is None or inventory[item] > inventory[max_item]:
                max_item = item
            if min_item is None or inventory[item] < inventory[min_item]:
                min_item = item

        print(f"Item most abundant: {max_item} with quantity {inventory[max_item]}")
        print(f"Item least abundant: {min_item} with quantity {inventory[min_item]}")
    else:
        print("No items in inventory to analyze.")

def add_new_item(inventory):
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    args = sys.argv[1:]

    inventory, order = parse_inventory(args)
    print_inventory_analysis(inventory, order)
    add_new_item(inventory)

if __name__ == "__main__":
    main()
