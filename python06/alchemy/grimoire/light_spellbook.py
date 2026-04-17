def light_spell_allowed_ingredients():
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str):
    spell_name.lower()
    from .light_validator import validate_ingredients
    if 'VALID' in validate_ingredients(ingredients):
        return 'spell recorded'
    return 'spell rejected'