import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
import helpers.utils as utils


class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        ingredient_index = burger.ingredients.index(ingredient)
        burger.remove_ingredient(ingredient_index)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        ingredient_index = burger.ingredients.index(ingredient)
        index = ingredient_index-1
        burger.move_ingredient(ingredient_index, index)
        assert burger.ingredients.index(ingredient) == index

    def test_get_price(self):
        price = utils.random_price()
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = price
        ingredient_mock.get_price.return_value = price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == price * 3

    def test_get_receipt_bun_name(self, burger):
        assert burger.bun.get_name() in burger.get_receipt()

    @pytest.mark.parametrize("index", [0, 1])
    def test_get_receipt_ingredient_name(self, burger, index):
        assert burger.ingredients[index].get_name() in burger.get_receipt()

    def test_get_receipt_price(self, burger):
        assert str(burger.get_price()) in burger.get_receipt()
