from locators.Main import Main
from .BasePage import BasePage

class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_categories_books(self):
        browser = self.driver
        browser.find_elements(*Main.menu_leftside.categories_books)[0].click()

    def click_shopping_cart(self):
        self._click(Main.header_links.link_shopping_cart)
