import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as types
import helpers.utils as utils


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = utils.random_name("bun")
    mock_bun.price = utils.random_price()
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = types.INGREDIENT_TYPE_FILLING
    mock_ingredient.name = utils.random_name("filling")
    mock_ingredient.price = utils.random_price()
    return mock_ingredient

@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(
        Bun(utils.random_name("bun"), utils.random_price()))
    burger.add_ingredient(
        Ingredient(types.INGREDIENT_TYPE_FILLING, utils.random_name("filling"), utils.random_price()))
    burger.add_ingredient(
        Ingredient(types.INGREDIENT_TYPE_SAUCE, utils.random_name("sauce"), utils.random_price()))
    return burger
