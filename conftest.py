from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# constant = {
#     "name":"Стілець обідній RYSLINGE білий/корич.",
#     "query":"RYSLINGE"
# }
#
#
# def group(lst, request):
#     if request in lst:
#         return lst[request]
#
#
# def testdata(request):
#     group(constant, request)