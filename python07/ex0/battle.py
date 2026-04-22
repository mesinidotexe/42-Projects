from ex0.ex0.factories import AquaFactory, FlameFactory


def test_factory(factory_class):
    print('Testing factory')
    factory = factory_class()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(type1, type2):
    print('Testing battle')
    flame_factory = type1()
    water_factory = type2()
    pokemon1 = flame_factory.create_base()
    pokemon2 = water_factory.create_base()
    print(pokemon1.describe())
    print('vs.')
    print(pokemon2.describe())
    print('fight!')
    print(pokemon1.attack())
    print(pokemon2.attack())


if __name__ == '__main__':
    test_factory(FlameFactory)
    print()
    test_factory(AquaFactory)
    print()
    fight(FlameFactory, AquaFactory)
