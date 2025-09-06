import random

import helpers.constants as const
import praktikum.ingredient_types as types


def random_name(name_type):
    name_sets = {
        "bun": const.BUN_NAMES,
        "filling": const.FILLING_NAMES,
        "sauce": const.SAUCES_NAMES
    }

    if name_type not in name_sets:
        raise ValueError(f"Неизвестный тип")

    return random.choice(name_sets[name_type])

def random_price():
    return random.uniform(1, 10000)

def random_types():
    ingredient_types = [types.INGREDIENT_TYPE_SAUCE, types.INGREDIENT_TYPE_FILLING]
    return random.choice(ingredient_types)
