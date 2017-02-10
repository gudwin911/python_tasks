from selenium import webdriver
from selenium.webdriver.common.by import By

'''driver = webdriver.Firefox()
driver.get("https://jysk.ua")
inputElement = driver.find_element_by_name("query")
inputElement.send_keys("RYSLINGE")
inputElement.submit()
outputElement = driver.find_elements(By.CLASS_NAME, "col-xs-12 col-ms-6 col-sm-4").count("col-xs-12 col-ms-6 col-sm-4")
print(outputElement)
assert outputElement == 8
driver.quit()
# .//*[@id='product-list-content']/div[3]/div[5]'''

for i in range(1, 10):
    print(".//*[@id='product-list-content']/div[3]/div[%s]" %i)
