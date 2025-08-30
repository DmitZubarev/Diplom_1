from praktikum.ingredient import Ingredient
import helpers.utils as utils


class TestIngredient:

    def test_get_price(self):
        ingredient_price = utils.random_price()
        ingredient = Ingredient(utils.random_types(), utils.random_name("filling" or "sauce"), ingredient_price)
        assert ingredient.get_price() == ingredient_price

    def test_get_name(self):
        ingredient_name = utils.random_name("filling" or "sauce")
        ingredient = Ingredient(utils.random_types(), ingredient_name, utils.random_price())
        assert ingredient.get_name() == ingredient_name

    def test_get_type(self):
        ingredient_type = utils.random_types()
        ingredient = Ingredient(ingredient_type, utils.random_name("filling" or "sauce"), utils.random_price())
        assert ingredient.get_type() == ingredient_type
