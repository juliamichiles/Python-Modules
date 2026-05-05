from .elements import create_air, create_earth
from elements import create_water, create_fire

def healing_potion() -> str:
    earth = create_earth()
    air = create_air()

    return f"Healing potion brewed with '{earth}' and '{air}'"


def strength_potion() -> str:
    water = create_water()
    fire = create_fire()

    return f"Strength potion brewed with '{fire}' and '{water}'"


