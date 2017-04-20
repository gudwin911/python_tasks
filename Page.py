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
