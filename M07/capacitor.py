#!/usr/bin/python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == '__main__':

    h_factory = HealingCreatureFactory()
    base_healer = h_factory.create_base()

    print("Testing Creature with healing capability")
    print(" base:")
    print(base_healer.describe())
    print(base_healer.attack())
    print(base_healer.heal('itself'))

    evolved_healer = h_factory.create_evolved()

    print(" evolved:")
    print(evolved_healer.describe())
    print(evolved_healer.attack())
    print(evolved_healer.heal('itself and others'))

    print()

    t_factory = TransformCreatureFactory()
    base_trans = t_factory.create_base()

    print("Testing Creature with transform capability")
    print(" base:")
    print(base_trans.describe())
    print(base_trans.attack())
    print(base_trans.transform())
    print(base_trans.attack())
    print(base_trans.revert())

    evolved_trans = t_factory.create_evolved()

    print(" evolved:")
    print(evolved_trans.describe())
    print(evolved_trans.attack())
    print(evolved_trans.transform())
    print(evolved_trans.attack())
    print(evolved_trans.revert())
