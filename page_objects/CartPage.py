from locators.Cart import Cart
from .BasePage import BasePage

class CartPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_link_product_shopping_cart(self):
        browser = self.driver
        browser.find_element(*Cart.product_link).click()

    def check_link_product_shopping_cart(self):
        browser = self.driver
        product_link = browser.find_element(*Cart.product_link).text
        return product_link
