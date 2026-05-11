from typing import cast
from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleError(Exception):
    ...


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            c_creature = cast(
                    Creature | TransformCapability, 
                    creature
            )  # all of this silent a mypy error...
            
            print(c_creature.transform())
            print(c_creature.attack())
            print(c_creature.revert())
        else:
            raise BattleError(
                    f"Invalid Creature '{creature.name}'"
                    " for this aggressive strategy"
                    )


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            c_creature = cast(
                    Creature | HealCapability,
                    creature
            )  # all of this silent a mypy error...
            print(c_creature.attack())
            print(c_creature.heal('itself'))
        else:
            raise BattleError(
                    f"Invalid Creature '{creature.name}'"
                    " for this defensive strategy"
                    )
