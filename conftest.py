from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def driver(request):
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
