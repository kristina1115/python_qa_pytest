from locators.Main import Main
from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_categories_books(self):
        self._click(Main.menu_leftside.categories_books, 0)

    def click_shopping_cart(self):
        self._click(Main.header_links.link_shopping_cart)

    def notification_display(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(Main.notification.notification_bar))

    def verify_message(self):
        return self._get_element_text(Main.notification.notification_bar_text)


