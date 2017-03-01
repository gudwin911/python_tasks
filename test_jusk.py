from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

'''def test_jusk1():
    driver = webdriver.Firefox()
    driver.get("https://jysk.ua")
    inputElement = driver.find_element_by_name("query")
    inputElement.send_keys("RYSLINGE")
    inputElement.submit()
    time.sleep(5)
    outputElement = driver.find_elements(By.CLASS_NAME, "product")
    assert len(outputElement) == 8
    driver.quit()'''

"""def test_jusk2():
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
    driver.quit()"""

# def test_jusk3(): # проверяем что вверху верно отображено название
#     driver = webdriver.Firefox()
#     driver.set_window_size(1440, 900)
#     driver.get("https://jysk.ua")
#     inputElement = driver.find_element_by_name("query")
#     inputElement.send_keys("RYSLINGE")
#     inputElement.submit()
#     time.sleep(5)
#     driver.find_element_by_xpath("//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']").click()
#     time.sleep(5)
#     elem = driver.find_element_by_class_name("widgets-enabled").text
#     assert elem == 'СТІЛ RYSLINGE + 4 СТІЛЬЦІ RYSLINGE'
#     driver.quit()

# def test_jusk4(): # проверяем что в описании есть текст “В комплект входять 2 додаткових "крила""
#     driver = webdriver.Firefox()
#     driver.get("https://jysk.ua")
#     inputElement = driver.find_element_by_name("query")
#     inputElement.send_keys("RYSLINGE")
#     inputElement.submit()
#     time.sleep(5)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     driver.find_element_by_xpath("//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']").click()
#     time.sleep(5)
#     elm = driver.find_element(By.CLASS_NAME, "product-specs").text
#     assert 'в комплекті з 2 додатковими "крилами"' in elm
#     driver.quit()

# def test_jusk5(): # проверяем, что есть 4 отзыва вверху
#     driver = webdriver.Firefox()
#     driver.get("https://jysk.ua")
#     inputElement = driver.find_element_by_name("query")
#     inputElement.send_keys("RYSLINGE")
#     inputElement.submit()
#     time.sleep(5)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     driver.find_element_by_xpath("//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']").click()
#     time.sleep(5)
#     elm = driver.find_element_by_class_name("review-count")
#     assert elm.text == "4 відгуків"
#     driver.quit()

# def test_jusk6(): # проверяем, что есть 4 отзыва, если нажать на видугки внизу
#     driver = webdriver.Firefox()
#     driver.get("https://jysk.ua")
#     inputElement = driver.find_element_by_name("query")
#     inputElement.send_keys("RYSLINGE")
#     inputElement.submit()
#     time.sleep(5)
#     driver.execute_script("window.scrollTo(0, 400);")
#     driver.find_element_by_xpath("//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']").click()
#     time.sleep(5)
#     driver.execute_script("window.scrollTo(0, 900);")
#     driver.find_element_by_xpath("//*[@id='content-tab-bar']/li[2]/a").click()
#     assert len(driver.find_elements_by_class_name("field-content")) == 4
#     driver.quit()

def test_jusk7(driver): # залышыты видгук...мем надислаты видгук, форма не закрылась и что чекбокс подсвечен красным
    #driver = webdriver.Firefox()
    driver.get("https://jysk.ua")
    inputElement = driver.find_element_by_name("query")
    inputElement.send_keys("RYSLINGE")
    inputElement.submit()
    #driver.find_element_by_xpath("//*[@id='CookieReportsBanner']/div/div[2]/a").click()
    # жду пока появится нужная мне имага стола
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Стіл RYSLINGE + 4 стільці RYSLINGE']")))
    driver.execute_script("window.scrollTo(0, 400);")
    driver.find_element_by_xpath("//*[@id='node-272253']/figure/a/img").click()
    # жду перехода страницу со столом
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='content-tab-bar']/li[2]/a")))
    driver.execute_script("window.scrollTo(0, 900);")
    # жму на вкладку "отзывы" внизу, жду пока вкладка откроется и жму "оставить отзыв"
    driver.find_element_by_xpath("//*[@id='content-tab-bar']/li[2]/a").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='product-ratings']/div/div/div/div/div/a")))
    driver.find_element_by_xpath("//*[@id='product-ratings']/div/div/div/div/div/a").click()
    # заполняем форму
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"edit-title")))
    driver.find_element(By.XPATH, "//*[@id='rating-select']/div/span[5]").click()
    driver.find_element_by_id("edit-title").send_keys("Title text")
    driver.find_element_by_id("edit-body").send_keys("thanks for these beautiful goods")
    driver.find_element_by_id("edit-author").send_keys("Ringo")
    driver.find_element_by_id("edit-age").click()
    driver.find_element_by_xpath("//*[@id='edit-age']/option[4]").click()
    driver.find_element_by_id("edit-sex").click()
    driver.find_element_by_xpath("//*[@id='edit-sex']/option[2]").click()
    driver.find_element_by_id("edit-city").send_keys("Detroit")
    driver.find_element_by_id("edit-email").send_keys("checkount@gmail.com")
    # отправляю отзыв, не подтвердив обработку личных данных
    driver.find_element_by_id("edit-submit--5").submit()
    # жду пока появится еррор-сообщение об обработке личных данных
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "validation-failed")))
    cls = driver.find_element(By.XPATH, "//*[@id='jysk-reviews-add-review-form']/div/div/div[9]").get_attribute("class")
    assert "not-validated" in cls
    #driver.quit()
