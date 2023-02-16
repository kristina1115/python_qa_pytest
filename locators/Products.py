from selenium.webdriver.common.by import By

class Products:
    class products_books:
        page_title = (By.CSS_SELECTOR, 'div.page-title > h1')
        page_sorting = (By.CSS_SELECTOR, 'div.product-sorting > span')
        page_sorting_select = (By.CSS_SELECTOR, '#products-orderby > option')
        page_display = (By.CSS_SELECTOR, 'div.product-page-size > span')
        page_display_select = (By.CSS_SELECTOR, '#products-pagesize > option')
        page_view = (By.CSS_SELECTOR, 'div.product-viewmode > span')
        page_view_select = (By.CSS_SELECTOR, '#products-viewmode > option')
        page_filter = (By.CSS_SELECTOR, 'div.filter-title > strong')
        page_filter_select = (By.CSS_SELECTOR, 'ul.price-range-selector > li')

    class product_card:
        button_add_to_card = (By.CSS_SELECTOR, "[value = 'Add to cart']")
        products_list = (By.CSS_SELECTOR, 'div.product-grid')
        product = (By.CSS_SELECTOR, products_list[1] + '> div.item-box')
        product_link = (By.CSS_SELECTOR, product[1] + ' ' + 'h2 > a')


