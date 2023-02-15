

class BasePage:
    def __init__(self, driver):
        self.driver=driver

    def __element(self, selector):
        return self.driver.find_element(selector)

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(*selector)).click().perform()