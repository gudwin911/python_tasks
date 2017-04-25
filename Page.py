from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def scroll_down(self, num):
        self.driver.execute_script("window.scrollTo(0, %s);" % num)

    def search(self, param1):
        txt = self.driver.find_element(By.NAME, "query")
        txt.send_keys(param1)
        txt.submit()
        return SearchResultPage(self.driver)


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://jysk.ua")
        self.driver.implicitly_wait(10)


class SearchResultPage(BasePage):

    def count_products(self, param1):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='%s']" % param1)))
        return len(self.driver.find_elements(By.CLASS_NAME, "product"))

    def to_product(self, param1):
        self.scroll_down(400)
        self.driver.find_element(By.XPATH, "//img[@alt='%s']" % param1).click()
        return ProductPage(self.driver)


class ProductPage(BasePage):
    def product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "widgets-enabled").text

    def product_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span[@itemprop='description']").text

    def header_review_quantity(self):
        return self.driver.find_element(By.CLASS_NAME, "review-count").text

    def open_reviews(self):
        self.scroll_down(900)
        self.driver.find_element(By.XPATH, "//*[@id='content-tab-bar']/li[2]/a").click()

    def reviews_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "field-content"))

    def btn_write_review(self):
        self.driver.find_element(By.XPATH, "//a[@href='#notification']").click()
        return ReviewPage(self.driver)


class ReviewPage(BasePage):

    def select_rating(self, num):
        self.driver.find_element(By.XPATH, "//*[@id='rating-select']/div/span[%s]" % num).click()

    def add_title(self, txt):
        self.driver.find_element(By.ID, "edit-title").send_keys(txt)

    def add_comment(self, txt):
        self.driver.find_element(By.ID, "edit-body").send_keys(txt)

    def add_author(self, name):
        self.driver.find_element(By.ID, "edit-author").send_keys(name)

    def select_age(self, option):
        self.driver.find_element(By.ID, "edit-age").click()
        self.driver.find_element(By.XPATH, "//*[@id='edit-age']/option[%s]" % option).click()

    def select_sex(self, sex):
        self.driver.find_element(By.ID, "edit-sex").click()
        self.driver.find_element(By.XPATH, "//*[@id='edit-sex']/option[@value='%s']" % sex).click()

    def add_city(self, city):
        self.driver.find_element(By.ID, "edit-city").send_keys(city)

    def add_mail(self, mail):
        self.driver.find_element(By.ID, "edit-email").send_keys(mail)

    def edit_accept_terms(self, bool):
        if bool:
            self.driver.find_element(By.ID, "edit-accept-terms").click()

    def send_review(self):
        self.driver.find_element(By.ID, "edit-submit").submit()

    def add_review(self, rating, title, txt, author, age, sex, city, mail, box):
        self.select_rating(rating).\
            add_title(title).\
            add_comment(txt).\
            add_author(author).\
            select_age(age).\
            select_sex(sex).\
            add_city(city).\
            add_mail(mail).\
            edit_accept_terms(box).\
            send_review()

    def get_error_msg_class(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "validation-failed")))
        return self.driver.find_element(By.XPATH, "//*[@id='jysk-reviews-add-review-form']/div/div/div[9]").\
            get_attribute("class")