from ex1.ex1.factories1 import HealingCreatureFactory, TransformCreatureFactory


def healing():
    print('Testing Creature with healing capability')
    heal = HealingCreatureFactory()
    base = heal.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print('evolved')
    evolved = heal.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transforming():
    print('Testing Creature with transform capability')
    transform = TransformCreatureFactory()
    base = transform.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.transformed_attack())
    print(base.revert())
    print('evolved')
    evolved = transform.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.transformed_attack())
    print(evolved.revert())


if __name__ == '__main__':
    # run with python3 -m ex1.capacitor from root
    healing()
    print()
    transforming()
