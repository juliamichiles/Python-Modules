from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        base_creature = Flameling("Flameling", "Fire")
        return base_creature

    def create_evolved(self) -> Creature:
        evolved_creature = Pyrodon("pyrodon", "Fire/Flying")
        return evolved_creature


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        base_creature = Aquabub("aquabub", "Water")
        return base_creature

    def create_evolved(self) -> Creature:
        evolved_creature = Torragon("Torragon", "Water")
        return evolved_creature
