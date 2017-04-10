from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://jysk.ua")

    def get_search_field(self):
        return self.driver.find_element_by_name("query")

    def input_text_in_search_field(self):
        self.get_search_field().send_keys("RYSLINGE")

    def submit_data_from_search_field(self):
        self.get_search_field().submit()


class SearchResultPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_search_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']")))

    def scroll_down_400(self):
        self.driver.execute_script("window.scrollTo(0, 400);")

    def get_some_product_img(self):
        return self.driver.find_element(By.XPATH, "//*[@id='node-272253']/figure/a/img")

    def click_on_product_img(self):
        self.get_some_product_img().click()


class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    def wait_for_content_download(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='content-tab-bar']/li[2]/a")))

    def scroll_down_900(self):
        self.driver.execute_script("window.scrollTo(0, 900);")

    def get_reviews_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='content-tab-bar']/li[2]/a")

    def wait_for_reviews_tab_visibility(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.id, "product-ratings")))

    def get_new_review_button(self):
        return self.driver.find_element(By.id, "product-ratings")


class ReviewPage():
    def __init__(self, driver):
        self.driver = driver

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