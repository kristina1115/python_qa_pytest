from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver=driver

    def _element(self, selector, index=0):
        return self.driver.find_elements(*selector)[index]

    def _elements(self, selector):
        return self.driver.find_elements(*selector)

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self._element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self._element(selector, index)
        element.clear()
        element.send_keys(value)

    def _get_element_text(self, selector, index=0):
        return self._element(selector, index).text