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

    fac1, strategy1 = opponents[0]
    fac2, strategy2 = opponents[1]

    poke1 = fac1.create_base()
    poke2 = fac2.create_base()

    print(f'{poke1.name} vs {poke2.name}')
    print(poke1.describe())
    print(poke2.describe())

    try:
        print(strategy1.act(poke1))
        if fac1 is HealingCreatureFactory:
            print(poke1.heal())
    except Exception as e:
        print(e)
        return
    try:
        print(strategy2.act(poke2))
    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    # run with python3 -m ex2.tournament from root
    normal = NormalStrategy()
    aggresive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    flame_fac = FlameFactory()
    water_fac = AquaFactory()
    heal_fac = HealingCreatureFactory()
    transform_fac = TransformCreatureFactory()

    print('Tournament 0 (basic)')
    first_fight = [
        (flame_fac, normal),
        (transform_fac, normal)
    ]
    tornament(first_fight)

    print()

    print('Tournament 1 (error)')
    second_fight = [
        (water_fac, aggresive),
        (heal_fac, defensive)
    ]
    tornament(second_fight)

    print()

    print('Tournament 2')
    third_fight = [
        (flame_fac, normal),
        (water_fac, normal)
    ]
    tornament(third_fight)

    print()

    print('Tournament 3')
    forth_fight = [
        (flame_fac, normal),
        (heal_fac, defensive)
    ]
    tornament(forth_fight)

    print()

    print('Tournament 4')
    fifth_fight = [
        (transform_fac, normal),
        (water_fac, aggresive)
    ]
    tornament(fifth_fight)

    print()

    print('Tournament 5')
    sixth_fight = [
        (transform_fac, normal),
        (heal_fac, defensive)
    ]
    tornament(sixth_fight)
