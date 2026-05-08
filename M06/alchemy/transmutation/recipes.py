import elements
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:

    s_potion = strength_potion()
    fire = elements.create_fire()
    air = create_air()

    gold = f"brew '{air}' and '{s_potion}' mixed with '{fire}'"
    return f"Recipe transmuting Lead to Gold: {gold}"
