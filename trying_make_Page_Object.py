from selenium import webdriver
import pytest

class HomePage():

    def __init__(self, driver):
        self.driver.get("https://jysk.ua")

    def get_search_field(self, driver):
        inputField = self.driver.find_element_by_name("query")
        return inputField

    def input_text_in_search_field(self):
        self.inputField.send_keys("RYSLINGE")

    def submit_data_from_search_field(self):
        self.inputField.submit()


    # def test_jusk7(self, driver): # залышыты видгук...мем надислаты видгук, форма не закрылась и что чекбокс подсвечен красным
    #     self.driver.get("https://jysk.ua")
    #     inputElement = self.driver.find_element_by_name("query")
    #     inputElement.send_keys("RYSLINGE")
    #     inputElement.submit()