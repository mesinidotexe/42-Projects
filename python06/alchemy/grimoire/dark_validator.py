def validate_ingredients(ingredients: str):
    from .dark_spellbook import __dark_spell_allowed_ingredients
    allowed = __dark_spell_allowed_ingredients()
    for ing in allowed:
        if ing == ingredients:
            return ingredients, 'VALID'
    return ingredients, 'INVALID'