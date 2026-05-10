#!/usr/bin/python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == '__main__':

    h_factory = HealingCreatureFactory()
    t_factory = TransformCreatureFactory()

    # base healing creature
    h_creature = h_factory.describe()
