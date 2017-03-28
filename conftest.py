from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
