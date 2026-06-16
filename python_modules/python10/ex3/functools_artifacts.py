from collections.abc import Callable
import functools
import operator
from typing import Any


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


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    
    @functools.singledispatch
    def check_type(spell_type: Any) -> str:
        return f'Unknown spell type {type(spell_type)}'
    
    @check_type.register
    def _(spell_type: int):
        return f'Damage spell: {spell_type} damage'
    
    @check_type.register
    def _(spell_type: str):
        return f'Enchantment: {spell_type}'
    
    @check_type.register
    def _(spell_type: list):
        return f'Multi-cast: {len(spell_type)}'
    
    return check_type


def enchantment() -> None:
    spells: dict[str, Callable] = partial_enchanter(base_enchantment)
    fire_spell = spells['fire']
    print(fire_spell('dragon'))
    ice_spell = spells['ice']
    print(ice_spell('mage'))
    lightning_spell = spells['lightning']
    print(lightning_spell('witch'))


def reducer() -> None:
    operations = ['add', 'multiply', 'max', 'min']
    print('Testing spell reducer...')
    print('Sum', spell_reducer([1, 2, 3, 4, 5], operations[0]))
    print('Product', spell_reducer([1, 2, 3, 4, 5], operations[1]))
    print('Max', spell_reducer([1, 2, 3, 4, 5], operations[2]))
    print('Min', spell_reducer([1, 2, 3, 4, 5], operations[3]))


def dispatcher():
    print('Testing spell dispatcher...')
    int_type: int = 42
    str_type: str = 'fireball'
    list_type: list = [
        'asd',
        {'key': 'Value'},
        67
    ]
    dict_type = {'Key': 'Value'}
    test = spell_dispatcher()
    print(test(int_type))
    print(test(str_type))
    print(test(list_type))
    print(test(dict_type))


def main() -> None:
    fibonacci_tests = [17, 11, 20]
    reducer()
    print()
    enchantment()
    print()
    for test in fibonacci_tests:
        print(memoized_fibonacci(test))
    print()
    dispatcher()
    

if __name__ == '__main__':
    main()
