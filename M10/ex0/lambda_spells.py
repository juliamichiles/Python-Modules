#!/usr/bin/env python3
# TODO: Should I add try/except blocks to each functions?


def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    # Sorts artifacts by ’power’ level (descending order)

    sorted_artifacts = sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
    )

    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    # Uses filter() to create a new list
    # containing only mages with power >= min_power

    powerful_mages = list(
            filter(
                lambda mage: mage['power'] >= min_power,
                mages
            )
    )

    return powerful_mages


def spell_transformer(spells: list[str]) -> list[str]:

    # Uses map() to apply the lambda func to all elements
    # in the list (add "* " prefix and " *" suffix)

    new_spells = list(map(
            lambda new: "* " + new + " *",
            spells
    ))

    return new_spells


def mage_stats(mages: list[dict]) -> dict:

    # Calculates statistics:
    # Most powerful mage’s power level
    # Least powerful mage’s power level
    # Average power level (rounded to 2 decimals)

    most_powerful = max(mages, key=lambda mage: mage['power'])
    least_powerful = min(mages, key=lambda mage: mage['power'])

    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    stats_dict = {
        'max_power': most_powerful["power"],
        'min_power': least_powerful["power"],
        'avg_power': avg_power
    }

    return stats_dict


def print_dicts(lst: list[dict]) -> None:

    for d in lst:
        items = [f"{key}: {value}" for key, value in d.items()]
        print(', '.join(items))


def main() -> None:

    artifacts = [
        {'name': 'Earth Shield', 'power': 85, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 84, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 77, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 76, 'type': 'focus'},
        {'name': 'Storm Crown', 'power': 106, 'type': 'relic'}
    ]

    mages = [
        {'name': 'River', 'power': 66, 'element': 'ice'},
        {'name': 'Phoenix', 'power': 92, 'element': 'light'},
        {'name': 'River', 'power': 74, 'element': 'shadow'},
        {'name': 'Phoenix', 'power': 67, 'element': 'lightning'},
        {'name': 'Alex', 'power': 58, 'element': 'light'}
    ]

    spells = ['shield', 'freeze', 'heal', 'lightning']

    print("\n===========================")
    print("==== * Lambda Spells * ====\n")
    print("Testing artifact sorter...")
    print("\n* Before *")
    print_dicts(artifacts)
    print("\n* After *")
    print_dicts(artifact_sorter(artifacts))
    print("\n===========================\n")
    print("Testing spell transformer...")
    print("\n* Before *")
    print(spells)
    print("\n* After *")
    print(spell_transformer(spells))
    print("\n===========================\n")
    print("Printing mage statistics:")
    print_dicts([mage_stats(mages)])
    print()


if __name__ == '__main__':
    main()
