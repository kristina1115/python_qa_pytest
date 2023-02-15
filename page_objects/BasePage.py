from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver=driver

    def __element(self, selector):
        return self.driver.find_element(*selector)

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _input(self, selector, value):
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)