from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients():
    return ['bats', 'frogs', 'aresenic', 'eyeball']


def dark_spell_record(spell_name: str, ingredients: str):
    spell_name.lower()
    if 'VALID' in validate_ingredients(ingredients):
        return 'spell recorded'
    return 'spell rejected'
