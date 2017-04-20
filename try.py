from python_tasks import Page
import pytest


class Test():
    name = "Стіл RYSLINGE + 4 стільці RYSLINGE"
    query = "RYSLINGE"

    def test_check_product_quantity(self, driver):
        product_quantity = Page.HomePage(driver).\
            search(self.query).\
            count_products(self.name)
        assert product_quantity == 8

    def test_check_product_name(self, driver):
        product_name = Page.HomePage(driver).\
            search(self.query).\
            to_product(self.name).\
            product_name()
        assert self.name in product_name

if __name__ == "__main__":
    pytest.main()
