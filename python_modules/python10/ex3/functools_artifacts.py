from collections.abc import Callable
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if not operation in ('add', 'multiply', 'max', 'min'):
        return None
    if operation == 'add':
        reduced_value = functools.reduce(operator.add, spells)
    elif operation == 'multiply':
        reduced_value = functools.reduce(operator.mul, spells)
    elif operation == 'max':
        reduced_value = functools.reduce(lambda x, y: y if x < y else x, spells)
    elif operation == 'min':
        reduced_value = functools.reduce(lambda x, y: y if x > y else x, spells)    
    return reduced_value


def base_enchantment(power: int, element: str, target: str) -> str: 
    return f'{element} spell {power}hp, hits {target}'


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': functools.partial(base_enchantment, 50, 'fire'),
        'ice': functools.partial(base_enchantment, 50, 'ice'),
        'lightning': functools.partial(base_enchantment, 50, 'lightning')
        }


def enchantment() -> None:
    spells = partial_enchanter(base_enchantment)
    fire_spell = spells['fire']
    print(fire_spell('dragon'))
    ice_spell = spells['ice']
    print(ice_spell('mage'))
    lightning_spell = spells['lightning']
    print(lightning_spell('witch'))


def reducer() -> None:
    print('Testing spell reducer...')
    print('Sum', spell_reducer([1, 2, 3, 4, 5], 'add'))
    print('Product', spell_reducer([1, 2, 3, 4, 5], 'multiply'))
    print('Max', spell_reducer([1, 2, 3, 4, 5], 'max'))
    print('Min', spell_reducer([1, 2, 3, 4, 5], 'min'))


def main() -> None:
    reducer()
    print()
    enchantment()


if __name__ == '__main__':
    main()
