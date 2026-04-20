def validate_ingredients(ingredients: str):
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    for ing in allowed:
        if ing == ingredients:
            return ingredients, 'VALID'
    return ingredients, 'INVALID'
