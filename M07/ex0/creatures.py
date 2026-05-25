from abc import ABC, abstractmethod
# add from typing import <...> ?


class Creature(ABC):

    def __init__(self, name: str, c_type: str) -> None:
        self.name = name.capitalize()
        self.type = c_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
