from python_tasks import Page
import pytest


class Test():
    def test_check_product_name(self, driver):
        home = Page.HomePage(driver)
        result = home.search("RYSLINGE")
        product_page = result.to_product("//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']")
        assert "Стіл RYSLINGE + 4 стільці RYSLINGE" in product_page.product_name()

if __name__ == "__main__":
    pytest.main()
