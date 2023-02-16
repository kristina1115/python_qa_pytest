from locators.Products import Products
from locators.Cart import Cart
from .BasePage import BasePage

class ProductsPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def search_elements_title(self):
        title = self._element(Products.products_books.page_title).text
        return title

    def search_elements_sorting(self):
        sorting = self._element(Products.products_books.page_sorting).text
        return sorting

    def search_elements_sorting_select(self):
        sorting_select = self._elements(Products.products_books.page_sorting_select)
        list_sorting = [i.text for i in sorting_select if len(i.text) > 0]
        return list_sorting


    def search_elements_display(self):
        display_per_page = self._element(Products.products_books.page_display, 0).text
        display_per_page_two = self._element(Products.products_books.page_display, 1).text
        return display_per_page + " " + display_per_page_two

    def search_elements_display_select(self):
        display_per_page_select = self._elements(Products.products_books.page_display_select)
        list_display = [i.text for i in display_per_page_select if len(i.text) > 0]
        return list_display

    def search_elements_view(self):
        view = self._element(Products.products_books.page_view).text
        return view

    def search_elements_view_select(self):
        view_select = self._elements(Products.products_books.page_view_select)
        list_view = [i.text for i in view_select if len(i.text) > 0]
        return list_view

    def search_elements_filter(self):
        filter = self._element(Products.products_books.page_filter).text
        return filter

    def search_elements_filter_select(self):
        filter_select = self._elements(Products.products_books.page_filter_select)
        list_filter = [i.text for i in filter_select if len(i.text) > 0]
        return list_filter

    def click_button_add_to_cart(self, index):
        self._click(Products.product_card.button_add_to_card, index)

    def click_link_product(self, index):
        product_from_list = self._element(Products.product_card.product, index)
        product_from_list._click(Products.product_card.product_link, 1)

    def check_link_product(self, index):
        product_from_list = self._element(Products.product_card.product, index)
        product_name = product_from_list.find_elements(*Products.product_card.product_link)[1].text
        return product_name

    def click_link_product_shopping_cart(self):
        self._click(Cart.product_link)

    def check_link_product_shopping_cart(self):
        self._element(Cart.product_link).text







