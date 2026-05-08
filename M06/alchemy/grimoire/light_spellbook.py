def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(
        spell_name: str,
        ingredients: str
        ) -> str:

    from .light_validator import validate_ingredients

    s_name = spell_name.capitalize()
    result_str = validate_ingredients(ingredients)

    if "INVALID" in result_str:
        return f"Spell rejected: {s_name} ({result_str})"
    else:
        return f"Spell recorded: {s_name} ({result_str})"
