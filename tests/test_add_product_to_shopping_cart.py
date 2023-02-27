import time


from page_objects.ProductsPage import ProductsPage
from page_objects.MainPage import MainPage
from page_objects.CartPage import CartPage


def test_add_product_to_shopping_cart(browser):
    # Переход на страницу Books
    ProductsPage(browser).open('https://demowebshop.tricentis.com')
    MainPage(browser).click_categories_books()
    # Название товара (первый в каталоге)
    link_product = ProductsPage(browser).get_product_link(0)
    # Добавить товар в корзину (первый товар в списке)
    ProductsPage(browser).click_button_add_to_cart(0)
    # Проверка уведомления
    MainPage(browser).verify_message('The product has been added to your shopping cart')
    # Зайти в корзину
    MainPage(browser).click_shopping_cart()
    # Проверка, что товар добавлен в корзину
    link_product_shopping_cart = CartPage(browser).check_link_product_shopping_cart()
    assert link_product == link_product_shopping_cart


def test_check_full_product_cart(browser):
    ProductsPage(browser).open('https://demowebshop.tricentis.com')
    MainPage(browser).click_categories_books()
    ProductsPage(browser).click_product_link(2)
    time.sleep(5)


