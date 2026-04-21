from ex0.ex0.factories import FlameFactory, AquaFactory
from ex1.ex1.factories1 import (HealingCreatureFactory,
                                TransformCreatureFactory)
from ex2.ex2.strategy import (NormalStrategy, AggressiveStrategy,
                              DefensiveStrategy)
from typing import List
# from ex1.ex1.capabilities import Sproutling, Bloomelle, Shiftling, Morphagon


def tornament(opponents: List):
    print('*** Tournament ***')
    print(f'{len(opponents)} opponents involved\n')
    print('* Battle *')

    first = True
    for opponent, _ in opponents:
        print(opponent.describe())
        if first:
            print('vs')
        else:
            print('now fight!')
        first = False

        for opponent, strategy in opponents:
            try:
                print(strategy.act(opponent))
            except Exception as e:
                print(e)
                return


if __name__ == '__main__':
    # run with python3 -m ex2.tournament from root
    normal = NormalStrategy()
    aggresive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    flame_fac = FlameFactory()
    flame_obj_base = flame_fac.create_base()

    water_fac = AquaFactory()
    water_obj_base = water_fac.create_base()

    heal_fac = HealingCreatureFactory()
    heal_obj_base = heal_fac.create_base()

    transform_fac = TransformCreatureFactory()
    transform_obj_base = transform_fac.create_base()

    print('Tournament 0 (basic)')
    first_fight = [
        (flame_obj_base, normal),
        (heal_obj_base, defensive)
    ]
    tornament(first_fight)

    print()

    print('Tournament 1 (error)')
    second_fight = [
        (flame_obj_base, aggresive),
        (heal_obj_base, defensive)
    ]
    tornament(second_fight)

    print()

    print('tournament 2 (aggressive)')
    third_fight = [
        (transform_obj_base, aggresive),
        (heal_obj_base, defensive)
    ]
    tornament(third_fight)
