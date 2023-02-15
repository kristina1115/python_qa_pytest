import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    print("/Browser was opened")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

