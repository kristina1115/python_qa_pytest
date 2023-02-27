import time
import pytest


from page_objects.ProductsPage import ProductsPage
from page_objects.MainPage import MainPage


@pytest.mark.parametrize('quantity', [0, -1, 'a', '!@#$%^&*"<,.', 10001])
def test_invalid_input_quantity_product(browser, quantity):
    # Переход на страницу Books
    ProductsPage(browser).open('https://demowebshop.tricentis.com')
    MainPage(browser).click_categories_books()
    # Переход в карточку товара (первый в каталоге)
    ProductsPage(browser).click_product_link(0)
    # Ввод невалидных данных
    ProductsPage(browser).input_quantity_product(quantity)
    # Добавление товара в корзину
    ProductsPage(browser).click_button_add_to_cart()
    # Проверка сообщения об ошибке
    message = MainPage(browser).verify_message_text()
    assert message == 'Quantity should be positive' or message == 'The maximum quantity allowed for purchase is 10000.'

