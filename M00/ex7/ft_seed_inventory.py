def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "grams":
        print(seed_type.capitalize(), 'seeds:', quantity, 'grams total')
    elif unit == "packets":
        print(seed_type.capitalize(), 'seeds:', quantity, 'packets available')
    elif unit == "area":
        print(seed_type.capitalize(), 'seeds:', end=" ")
        print('covers', quantity, 'square meters')
    else:
        print('Unknown unit type')
