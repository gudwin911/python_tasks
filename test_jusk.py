from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_jusk1():
    driver = webdriver.Firefox()
    driver.get("https://jysk.ua")
    inputElement = driver.find_element_by_name("query")
    inputElement.send_keys("RYSLINGE")
    inputElement.submit()
    time.sleep(5)
    outputElement = driver.find_elements(By.CLASS_NAME, "product")
    assert len(outputElement) == 8
    driver.quit()

def test_jusk2():
    driver = webdriver.Firefox()
    driver.get("https://jysk.ua")
    inputElement = driver.find_element_by_name("query")
    inputElement.send_keys("RYSLINGE")
    inputElement.submit()
    time.sleep(5)
    count = 1
    while True:
        try:
            driver.find_element(By.XPATH, "//*[@id='product-list-content']/div[3]/div[%s]" % count)
            count += 1
        except:
            count -= 1
            break

    assert count == 8
    driver.quit()
