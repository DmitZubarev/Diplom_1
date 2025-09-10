from praktikum.bun import Bun
import helpers.utils as utils


class TestBun:

    def test_get_name(self):
        bun_name = utils.random_name("bun")
        bun = Bun(bun_name, utils.random_price())
        assert bun.get_name() == bun_name

    def test_get_price(self):
        bun_price = utils.random_price()
        bun = Bun(utils.random_name("bun"), bun_price)
        assert bun.get_price() == bun_price
