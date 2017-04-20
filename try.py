from python_tasks import Page

class s():
    def test_y(self):
        page = Page.HomePage
        page.get_search_field().send_keys("RYSLINGE").submit()
        page = Page.SearchResultPage
        page.wait_search_result()
        page.scroll_down(400)
        page.get_product_img().click()
        page = Page.ProductPage
        page.wait_for_content_download()
        txt = page.get_product_name()
        assert txt == "СТІЛ RYSLINGE + 4 СТІЛЬЦІ RYSLINGE"