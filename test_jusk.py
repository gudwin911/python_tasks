from python_tasks import Page
import pytest

# все эти переменные нужно вынести в отдельный файл и использовать параметризацию как на строке 27
# но я еще не придумал как это сделать красиво чтобы чтобы функция сама находила нужные переменные из списка
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


def product_page(driver, query, name):
    return Page.HomePage(driver).\
            search(query).\
            to_product(name)


# 1 проверяем что количество товаров по запросу равно 8
@pytest.mark.parametrize("query,name", [("RYSLINGE", "Стілець обідній RYSLINGE білий/корич.")])
def test_check_product_quantity(driver, query, name):
    product_quantity = Page.HomePage(driver).\
        search(query).\
        count_products(name)
    assert product_quantity == 8


# 2 проверяем что вверху верно отображено название
def test_check_product_name(driver, query, name):
    product_name = product_page(driver, query, name).\
        product_name()
    assert name == product_name


# 3 проверяем что в описании есть текст “В комплект входять 2 додаткових 'крила'"
def test_check_product_description(driver, query, name):
    description = product_page(driver, query, name).\
        product_description()
    assert 'кольори: білий, коричневий' in description


# 4 проверяем, что есть 4 отзыва вверху
def test_check_reviews_quantity_header(driver, query, name):
    quantity = product_page(driver, query, name).\
        header_review_quantity()
    assert quantity == "8 відгуків"


# 5 проверяем, что есть 4 отзыва, если нажать на видугки внизу
def test_check_reviews_counter(driver, query, name):
    quantity = product_page(driver, query, name).\
        open_reviews().\
        reviews_count()
    assert quantity == 8


# 6 залышыты видгук...мем надислаты видгук, форма не закрылась и что чекбокс подсвечен красным
def test_check_review_checkbox_error_message(driver, query, name, rating,
                                             title, txt, author, age, sex, city, mail, box):
    error = product_page(driver, query, name).\
        open_reviews().\
        btn_write_review().\
        add_review(rating, title, txt, author,
                   age, sex, city, mail, box).\
        get_error_msg_class()
    assert "not-validated" in error


if __name__ == "__main__":
    pytest.main()
