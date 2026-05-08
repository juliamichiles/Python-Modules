from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(
        spell_name: str,
        ingredients: str
        ) -> str:

    s_name = spell_name.capitalize()
    result_str = validate_dark_ingredients(ingredients)

    if "INVALID" in result_str:
        return f"Spell rejected: {s_name} ({result_str})"
    else:
        return f"Spell recorded: {s_name} ({result_str})"
