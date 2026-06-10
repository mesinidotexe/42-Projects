from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    
    def combined(target: str, power: int):
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    
    def checking(target: str, power: int) -> str:
        if condition(target, power):
            new_spell = spell(target, power)
            return new_spell
        else:
            return "Spell fizzled"
    return checking


def spell_sequence(spells: list[Callable]) -> Callable:

    def s_sequence(target: str, power: int) -> str:
        sequence = []
        for spell in spells:
            sequence.append(spell(target, power))
        return sequence
    return s_sequence


def fireball(target: str, power: int) -> str:
    return f'{target} Fireballed him causing {power} damage'


def heal(target: str, power: int) -> str:
    return f'{target} healed in {power} hp'


def def_condition(target: str, power: int) -> str:
    target.capitalize()
    if power >= 10:
        return True
    return False


def new_spell(target: str, power: int) -> str:
    return f'{target} killed monster by causing {power} damage'


def main():
    test_values = [5, 17, 11]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined = spell_combiner(fireball, heal)
    print(combined(test_targets[0], test_values[1]))

    print()

    amplifed = power_amplifier(fireball, 3)
    print(amplifed(test_targets[1], test_values[2]))

    print()

    condition = conditional_caster(def_condition, new_spell)
    print(condition(test_targets[2], test_values[0]))
    print(condition(test_targets[3], test_values[1]))

    print()

    all_spells = [combined,
                  amplifed,
                  condition
                  ]
    seq = spell_sequence(all_spells)
    print(seq(test_targets[0], test_values[2]))


if __name__ == '__main__':
    main()