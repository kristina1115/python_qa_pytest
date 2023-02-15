from page_objects.CommonPage import CommonPage
import time

def test_login(browser):
    CommonPage(browser).open('https://demowebshop.tricentis.com')
    CommonPage(browser).login_user('kr@mail.ru', '123456')
    time.sleep(5)
    print("Everything is ok!")