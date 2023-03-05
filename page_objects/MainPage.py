from locators.Main import Main
from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_categories_books(self):
        self._click(Main.menu_leftside.categories_books, 0)

    def click_shopping_cart(self):
        self._click(Main.header_links.link_shopping_cart)

    def verify_message(self, text):
        return WebDriverWait(self.driver, 2).until(EC.text_to_be_present_in_element(Main.notification.notification_bar, text))

    def verify_message_text(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(Main.notification.notification_bar_text))
        return self._get_element_text(Main.notification.notification_bar_text)




