from selenium.webdriver.common.by import By

class Main:
    class menu_leftside:
        categories_books = (By.CSS_SELECTOR, 'ul.list > li > a')

    class header_links:
        link_shopping_cart = (By.CSS_SELECTOR, '#topcartlink > a')