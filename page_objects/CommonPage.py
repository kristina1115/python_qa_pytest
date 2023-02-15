from locators.Common import Common
from .BasePage import BasePage


class CommonPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def login_user(self, email, password):
        self._input(Common.user_login.email_input, email)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.loggin_button)
        return self





