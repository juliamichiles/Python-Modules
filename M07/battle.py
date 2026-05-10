#!/usr/bin/python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:

    creature = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(creature.describe())
    print(creature.attack())
    print(evolved.describe())
    print(f"{evolved.attack()}\n")


def test_battle(
        fact_1: CreatureFactory,
        fact_2: CreatureFactory
        ) -> None:

    creat_1 = fact_1.create_base()
    creat_2 = fact_2.create_base()

    print("Testing battle")
    print(f"{creat_1.describe()}\nvs.\n{creat_2.describe()}\nfight!")
    print(creat_1.attack())
    print(creat_2.attack())


if __name__ == '__main__':

    f_factory = FlameFactory()
    a_factory = AquaFactory()
    test_factory(f_factory)
    test_factory(a_factory)
    test_battle(f_factory, a_factory)
