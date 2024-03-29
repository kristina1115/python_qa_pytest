from locators.Cart import Cart
from .BasePage import BasePage

class CartPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_link_product_shopping_cart(self):
        self._click(Cart.product_link)

    def check_link_product_shopping_cart(self):
        product_link = self._element(Cart.product_link).text
        return product_link
