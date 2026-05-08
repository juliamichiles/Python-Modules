from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:

    allowed = dark_spell_allowed_ingredients()
    lower_ingr = ingredients.lower()

    for item in allowed:
        if item in lower_ingr:
            return f"VALID - {ingredients}"

    return f"INVALID - {ingredients}"
