from selenium.webdriver.common.by import By

class Cart:
    product = (By.CSS_SELECTOR, 'tbody > tr')
    product_link = (By.CSS_SELECTOR, product[1] + ' ' + 'td.product > a')