#!/usr/bin/python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == '__main__':

    h_factory = HealingCreatureFactory()
    base_healer = h_factory.create_base()

    print("Testing Creature with healing capability")
    print(" base:")
    print(f"{base_healer.describe()}")
    print(f"{base_healer.attack()}")
    print(f"{base_healer.heal('itself')}")

    evolved_healer = h_factory.create_evolved()

    print(" evolved:")
    print(f"{evolved_healer.describe()}")
    print(f"{evolved_healer.attack()}")
    print(f"{evolved_healer.heal('itself and others')}")

    print()

    t_factory = TransformCreatureFactory()
    base_trans = t_factory.create_base()

    print("Testing Creature with transform capability")
    print(" base:")
    print(f"{base_trans.describe()}")
    print(f"{base_trans.attack()}")
    print(f"{base_trans.transform()}")
    print(f"{base_trans.attack()}")
    print(f"{base_trans.revert()}")

    evolved_trans = t_factory.create_evolved()

    print(" evolved:")
    print(f"{evolved_trans.describe()}")
    print(f"{evolved_trans.attack()}")
    print(f"{evolved_trans.transform()}")
    print(f"{evolved_trans.attack()}")
    print(f"{evolved_trans.revert()}")

