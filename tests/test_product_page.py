import time


from page_objects.ProductsPage import ProductsPage
from page_objects.MainPage import MainPage

def test_check_elements_books_page(browser):
    # Переход на страницу Books
    ProductsPage(browser).open('https://demowebshop.tricentis.com')
    MainPage(browser).click_categories_books()

    # Проверка названия страницы
    title = ProductsPage(browser).search_elements_title()
    assert title == "Books"

    # Сортировка. Проверка названия и выпадающего списка
    sorting = ProductsPage(browser).search_elements_sorting()
    assert sorting == "Sort by"
    elements_sorting = ProductsPage(browser).search_elements_sorting_select()
    assert "Position" and "Name: A to Z" and "Name: Z to A" and "Price: Low to High" and "Price: High to Low" and "Created on" in elements_sorting

    # Количество товаров на странице. Проверка названия и выпадающего списка
    display_per_page = ProductsPage(browser).search_elements_display()
    assert display_per_page == "Display per page"
    elements_display = ProductsPage(browser).search_elements_display_select()
    assert "4" and "8" and "12" in elements_display

    # Расположение карточек товаров на странице. Проверка названия и выпадающего списка
    view = ProductsPage(browser).search_elements_view()
    assert view == "View as"
    elements_view = ProductsPage(browser).search_elements_view_select()
    assert "Grid" and "List" in elements_view

    # Фильтр. Проверка названия и списка
    filter_by_price = ProductsPage(browser).search_elements_filter()
    assert filter_by_price == "Filter by price"
    elements_filter = ProductsPage(browser).search_elements_filter_select()
    assert "Under 25.00" and "25.00 - 50.00" and "Over 50.00" in elements_filter
    print(elements_filter)

def test_check_full_product_cart(browser):
    ProductsPage(browser).open('https://demowebshop.tricentis.com')
    MainPage(browser).click_categories_books()
    ProductsPage(browser).click_product_link(2)
    time.sleep(5)






