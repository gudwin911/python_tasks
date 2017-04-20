from selenium.webdriver.common.by import By


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
    def to_product(self, param1):
        self.scroll_down(400)
        self.driver.find_element(By.XPATH, param1).click()
        return ProductPage(self.driver)


class ProductPage(BasePage):
    def product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "widgets-enabled").text
