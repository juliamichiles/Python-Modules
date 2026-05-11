from typing import Any
from ex0.factory import CreatureFactory
from .special_creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Any:
        base_creature = Shiftling("Shiftling", "Normal")
        return base_creature

    def create_evolved(self) -> Any:
        evolved_creature = Morphagon("Morphagon", "Normal/Dragon")
        return evolved_creature


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Any:
        base_creature = Sproutling("Sproutling", "Grass")
        return base_creature

    def create_evolved(self) -> Any:
        evolved_creature = Bloomelle("Bloomelle", "Grass/Fairy")
        return evolved_creature
