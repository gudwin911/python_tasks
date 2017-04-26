from python_tasks import Page
import pytest


class Test():
    name = "Стілець обідній RYSLINGE білий/корич."
    query = "RYSLINGE"
    # review data
    rating = 5
    title = "Title"
    txt = "Some text"
    author = "Greber"
    age = 3
    sex = "male"
    city = "London"
    mail = "chekount@gmail.com"
    box = False

    def product_page(self, driver):
        return Page.HomePage(driver).\
                search(self.query).\
                to_product(self.name)

    # 1 проверяем что количество товаров по запросу равно 8
    def test_check_product_quantity(self, driver):
        product_quantity = Page.HomePage(driver).\
            search(self.query).\
            count_products(self.name)
        assert product_quantity == 8

    # 2 проверяем что вверху верно отображено название
    def test_check_product_name(self, driver):
        product_name = self.product_page(driver).\
            product_name()
        assert self.name in product_name

    # 3 проверяем что в описании есть текст “В комплект входять 2 додаткових 'крила'"
    def test_check_product_description(self, driver):
        description = self.product_page(driver).\
            product_description()
        assert 'кольори: білий, коричневий' in description

    # 4 проверяем, что есть 4 отзыва вверху
    def test_check_reviews_quantity_header(self, driver):
        quantity = self.product_page(driver).\
            header_review_quantity()
        assert quantity == "8 відгуків"

    # 5 проверяем, что есть 4 отзыва, если нажать на видугки внизу
    def test_check_reviews_counter(self, driver):
        quantity = self.product_page(driver).\
            open_reviews().\
            reviews_count()
        assert quantity == 8

    # 6 залышыты видгук...мем надислаты видгук, форма не закрылась и что чекбокс подсвечен красным
    def test_check_review_checkbox_error_message(self, driver):
        error = self.product_page(driver).\
            open_reviews().\
            btn_write_review().\
            add_review(self.rating, self.title, self.txt, self.author,
                       self.age, self.sex, self.city, self.mail, self.box).\
            get_error_msg_class()
        assert "not-validated" in error


if __name__ == "__main__":
    pytest.main()
