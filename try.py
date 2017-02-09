from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("https://jysk.ua")
inputElement = driver.find_element_by_name("query")
inputElement.send_keys("RYSLINGE")
inputElement.submit()
# после этого кода ничего не выполняется/не находится
# не понимаю, почему, попытка "ждать" в вар 2 тоже ни к чему не приводит, где я ошибаюсь?
# col-xs-12 col-ms-6 col-sm-4 это название класса контейнера с найденным поиком товаром

""" var 1 - не находит элемент
outputElement = driver.find_elements(By.CLASS_NAME, "col-xs-12 col-ms-6 col-sm-4")#.count("col-xs-12 col-ms-6 col-sm-4")
assert outputElement == 8
"""

""" var 2 - все время срабатывает except, не находит элемент
try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(driver.find_elements_by_class_name("col-xs-12 col-ms-6 col-sm-4")))
    assert elem.count() == 8
except TimeoutException:
    print("Loading took too much time!")
"""

""" var 3 - пытаюсь пройтись по номерации "дивов" от 1 до 9, тк должно быть 8 результатов поиска, 9й как проверка, что их не больше
выдает ошибку AssertionError 0==8, не находит объекты
# //*[@id='product-list-content']/div[3]/div[1] путь к найденному товару
count = 0
outputElement = ""
for i in range(1, 10):
    if outputElement:
        outputElement = driver.find_elements(By.XPATH, "//*[@id='product-list-content']/div[3]/div[%s]" %i)
        count +=1
    else:
        break

assert count == 8
"""
driver.close()
