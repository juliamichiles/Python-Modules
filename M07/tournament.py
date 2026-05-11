#!/usr/bin/python3
from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
        DefensiveStrategy,
        AggressiveStrategy,
        NormalStrategy,
        BattleError,
        BattleStrategy
)


def battle(opponents: List[Tuple[
            CreatureFactory,
            BattleStrategy
        ]]) -> None:

    op_count = len(opponents)
    print(f"*** Tournament ***\n{op_count} opponents involved")
    try:
        for i in range(op_count):
            for j in range(i + 1, op_count):
                # starts from i + 1 to op_count
                fact_1, strat_1 = opponents[i]
                fact_2, strat_2 = opponents[j]

                c_1 = fact_1.create_base()
                c_2 = fact_2.create_base()

                print("\n* Battle *")
                print(f"{c_1.describe()}\n vs.\n{c_2.describe()}\n now fight!")

                strat_1.act(c_1)
                strat_2.act(c_2)

    except BattleError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == '__main__':

    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    normal_s = NormalStrategy()
    aggressive_s = AggressiveStrategy()
    defensive_s = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_0 = [
            (flame_f, normal_s),
            (heal_f, defensive_s)
    ]
    battle(opponents_0)

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_1 = [
        (flame_f, aggressive_s),
        (heal_f, defensive_s)
    ]
    battle(opponents_1)

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_2 = [
        (aqua_f, normal_s),
        (heal_f, defensive_s),
        (trans_f, aggressive_s)
        # (flame_f, normal_s),  # if uncomment, add a comma to the line above
        # (heal_f, defensive_s),
        # (trans_f, normal_s)
    ]
    battle(opponents_2)
