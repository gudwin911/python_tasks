from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from python_tasks import locators


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_search_field(self):
        return self.driver.find_element(By.NAME("query"))

    def scroll_down(self, num):
        self.driver.execute_script("window.scrollTo(0, %s);" % num)

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://jysk.ua")

class SearchResultPage(BasePage):

    def wait_search_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "view-header")))

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "product")

    def get_product_img(self):
         return self.driver.find_element(By.XPATH, "//div[@class='col-ms-6']//img[1]")

class ProductPage(BasePage):
    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "widgets-enabled").text

    def get_product_specs(self):
        return self.driver.find_element(By.CLASS_NAME, "product-specs").text


    def wait_for_content_download(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='content-tab-bar']/li[2]/a")))

    def get_reviews_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='content-tab-bar']/li[2]/a")

    def wait_for_reviews_tab_visibility(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "product-ratings")))

    def get_new_review_button(self):
        return self.driver.find_element(By.ID, "product-ratings")


class ReviewPage(BasePage):

    def wait_for_content_download(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "edit-title")))

    def get_select_rating_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='rating-select']/div/span[5]")

    def get_review_title(self):
        return self.driver.find_element_by_id("edit-title")

    def get_review_text(self):
        return self.driver.find_element_by_id("edit-body")

    def get_review_author(self):
        return self.driver.find_element_by_id("edit-author")

    def get_review_age_dropbox(self):
        return self.driver.find_element_by_id("edit-age")

    def get_review_age_option(self):
        return self.driver.find_element_by_xpath("//*[@id='edit-age']/option[4]")

    def get_review_sex_dropbox(self):
        return self.driver.find_element_by_id("edit-sex")

    def get_review_sex_option(self):
        return self.driver.find_element_by_xpath("//*[@id='edit-sex']/option[2]")

    def get_review_city(self):
        return self.driver.find_element_by_id("edit-city")

    def get_review_email(self):
        return self.driver.find_element_by_id("edit-email")

    def get_review_submit(self):
        return self.driver.find_element_by_id("edit-submit--4")

    def wait_validation_error(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "validation-failed")))

    def get_personal_data_checkbox(self):
        return self.driver.find_element(By.XPATH, "//*[@id='jysk-reviews-add-review-form']/div/div/div[9]")