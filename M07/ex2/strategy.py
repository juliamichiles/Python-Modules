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
            t_creature = cast(TransformCapability, creature)
            print(t_creature.transform())
            print(creature.attack())
            print(t_creature.revert())
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
            h_creature = cast(HealCapability, creature)
            print(creature.attack())
            print(h_creature.heal('itself'))
        else:
            raise BattleError(
                    f"Invalid Creature '{creature.name}'"
                    " for this defensive strategy"
                    )
