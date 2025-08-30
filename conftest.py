import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as types
import helpers.utils as utils


@pytest.fixture()
def bun():
    return Bun(utils.random_name("bun"), utils.random_price())

@pytest.fixture()
def filling():
    return Ingredient(types.INGREDIENT_TYPE_FILLING, utils.random_name("filling"), utils.random_price())

@pytest.fixture()
def sauce():
    return Ingredient(types.INGREDIENT_TYPE_SAUCE, utils.random_name("sauce"), utils.random_price())

@pytest.fixture()
def ingredient():
    ingredient_price = utils.random_price()
    ingredient_type = utils.random_types()
    if ingredient_type == "FILLING":
        ingredient_name = utils.random_name("filling")
    else:
        ingredient_name = utils.random_name("sauce")
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)

@pytest.fixture()
def burger(bun, sauce, filling):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(filling)
    burger.add_ingredient(sauce)
    return burger
