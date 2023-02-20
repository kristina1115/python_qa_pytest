from selenium.webdriver.common.by import By

class Main:
    class menu_leftside:
        categories_books = (By.CSS_SELECTOR, 'ul.list > li > a')

    class header_links:
        link_shopping_cart = (By.CSS_SELECTOR, '#topcartlink > a')

    class notification:
        notification_bar = (By.ID, 'bar-notification')
        notification_bar_text = (By.CSS_SELECTOR, 'p.content')
        notification_bar_link = (By.CSS_SELECTOR, notification_bar_text[1] + ' > a')