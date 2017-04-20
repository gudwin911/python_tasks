from python_tasks import Page
import pytest

# class s():
#     def testy(self):
#         page = Page.HomePage
#         page.get_search_field().send_keys("RYSLINGE").submit()
#         page = Page.SearchResultPage
#         page.wait_search_result()
#         page.scroll_down(400)
#         page.get_product_img().click()
#         page = Page.ProductPage
#         page.wait_for_content_download()
#         txt = page.get_product_name()
#         assert txt == "СТІЛ RYSLINGE + 4 СТІЛЬЦІ RYSLINGE"

class Test(pytest):
    def test_check_product_name(self):
        home = Page.HomePage(self.driver)
        result = home.search("RYSLINGE")
        product_page = result.to_product("//div[@class='col-ms-6']//img[1]")
        assert "СТІЛ RYSLINGE + 4 СТІЛЬЦІ RYSLINGE" in product_page.product_name()