from typing import Any, List
from collections.abc import Callable


def mage_counter() -> Callable:
    x: int = 0

    def inner() -> int:
        nonlocal x
        x += 1
        return x

    return inner


def spell_accumulator(initial_power: int) -> Callable:

    def inner(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power

    return inner


def enchantment_factory(enchantment_type: str) -> Callable:
    string: str = ''

    def inner(item: str) -> str:
        nonlocal string
        string = f'{enchantment_type}_{item}'
        return string

    return inner


def memory_vault() -> dict[str, Callable]:
    data: List = {}

    def store(key: str, value: Any) -> None:
        nonlocal data
        data[key] = value
    
    def recall(key: str) -> Any:
        if key in data:
            return data[key]
        return 'Memory not found'
    
    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    print('Testing mage counter...')
    count1 = mage_counter()
    count2 = mage_counter()
    print('counter_a call 1:', count1())
    print('counter_a call 2:', count1())
    print('countet_b call 1:', count2())

    print()

    accumulator = spell_accumulator(100)
    print('Base 100, add 20:', accumulator(20))
    print('Base 100, add 30:', accumulator(30))

    print()

    print('Testing enchantment factory...')
    ench_type1 = enchantment_factory('Flaming')
    ench_type2 = enchantment_factory('Frozen')
    print(ench_type1('Sword'))
    print(ench_type2('Shield'))

    print()

    print('Testing memory vault...')
    key = 'secret'
    value = 42
    vault = memory_vault()
    vault['store'](key, value)
