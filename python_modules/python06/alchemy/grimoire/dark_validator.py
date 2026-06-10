from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    for ing in allowed:
        if ing == ingredients:
            return ingredients, 'VALID'
    return ingredients, 'INVALID'
