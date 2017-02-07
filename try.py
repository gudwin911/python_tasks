from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://jysk.ua")
inputElement = driver.find_element_by_name("query")
inputElement.send_keys("RYSLINGE")
inputElement.submit()
try:
    WebDriverWait(driver, 5)
    outputElement = driver.find_element(By.XPATH, ".//*[@id='product-list-content']/div[1]/h1/span")
    assert outputElement == "8"
finally:
    driver.quit()