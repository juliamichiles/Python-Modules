from .capability import TransformCapability, HealCapability
from ex0.creatures import Creature


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, c_type: str) -> None:
        Creature.__init__(self, name, c_type)

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a small amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, c_type: str) -> None:
        Creature.__init__(self, name, c_type)

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):

    def __init__(self, name: str, c_type: str) -> None:
        Creature.__init__(self, name, c_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):

    def __init__(self, name: str, c_type: str) -> None:
        Creature.__init__(self, name, c_type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
