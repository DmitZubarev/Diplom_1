import pytest

from praktikum.burger import Burger
import helpers.utils as utils


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        ingredient_index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(ingredient_index)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        ingredient_index = burger.ingredients.index(mock_ingredient)
        index = ingredient_index-1
        burger.move_ingredient(ingredient_index, index)
        assert burger.ingredients.index(mock_ingredient) == index

    def test_get_price(self, mock_bun, mock_ingredient):
        price = utils.random_price()
        mock_bun.get_price.return_value = price
        mock_ingredient.get_price.return_value = price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == price * 3

    def test_get_receipt_bun_name(self, burger):
        assert burger.bun.get_name() in burger.get_receipt()

    @pytest.mark.parametrize("index", [0, 1])
    def test_get_receipt_ingredient_name(self, burger, index):
        assert burger.ingredients[index].get_name() in burger.get_receipt()

    def test_get_receipt_price(self, burger):
        assert str(burger.get_price()) in burger.get_receipt()
