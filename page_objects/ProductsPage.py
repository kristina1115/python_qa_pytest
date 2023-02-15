from locators.Products import Products
from locators.Cart import Cart
from .BasePage import BasePage

class ProductsPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def search_elements_title(self):
        browser = self.driver
        title = browser.find_element(*Products.products_books.page_title).text
        return title

    def search_elements_sorting(self):
        browser = self.driver
        sorting = browser.find_element(*Products.products_books.page_sorting).text
        return sorting

    def search_elements_sorting_select(self):
        browser = self.driver
        sorting_select = browser.find_elements(*Products.products_books.page_sorting_select)
        list_sorting = [i.text for i in sorting_select if len(i.text) > 0]
        return list_sorting


    def search_elements_display(self):
        browser = self.driver
        display_per_page = browser.find_elements(*Products.products_books.page_display)[0].text
        display_per_page_two = browser.find_elements(*Products.products_books.page_display)[1].text
        return display_per_page + " " + display_per_page_two

    def search_elements_display_select(self):
        browser = self.driver
        display_per_page_select = browser.find_elements(*Products.products_books.page_display_select)
        list_display = [i.text for i in display_per_page_select if len(i.text) > 0]
        return list_display

    def search_elements_view(self):
        browser = self.driver
        view = browser.find_element(*Products.products_books.page_view).text
        return view

    def search_elements_view_select(self):
        browser = self.driver
        view_select = browser.find_elements(*Products.products_books.page_view_select)
        list_view = [i.text for i in view_select if len(i.text) > 0]
        return list_view

    def search_elements_filter(self):
        browser = self.driver
        filter = browser.find_element(*Products.products_books.page_filter).text
        return filter

    def search_elements_filter_select(self):
        browser = self.driver
        filter_select = browser.find_elements(*Products.products_books.page_filter_select)
        list_filter = [i.text for i in filter_select if len(i.text) > 0]
        return list_filter

    def click_button_add_to_cart(self, index):
        browser = self.driver
        browser.find_elements(*Products.product_card.button_add_to_card)[index].click()

    def click_link_product(self, index):
        browser = self.driver
        product_from_list = browser.find_elements(*Products.product_card.product)[index]
        product_from_list.find_elements(*Products.product_card.product_link)[1].click()

    def check_link_product(self, index):
        browser = self.driver
        product_from_list = browser.find_elements(*Products.product_card.product)[index]
        product_name = product_from_list.find_elements(*Products.product_card.product_link)[1].text
        return product_name

    def click_link_product_shopping_cart(self):
        browser = self.driver
        browser.find_element(*Cart.product_link).click()

    def check_link_product_shopping_cart(self):
        browser = self.driver
        browser.find_element(*Cart.product_link).text







