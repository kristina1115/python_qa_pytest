from locators.Common import Common
from .BasePage import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        self.driver=driver
        self.path='/login'

    def open(self, url):
        self.driver.get(url + self.path)

    def login_user(self, email, password):
        browser = self.driver
        browser.find_element(*Common.user_login.email_input).clear()
        browser.find_element(*Common.user_login.email_input).send_keys(email)
        browser.find_element(*Common.user_login.password_input).clear()
        browser.find_element(*Common.user_login.password_input).send_keys(password)
        browser.find_element(*Common.user_login.loggin_button).click()





