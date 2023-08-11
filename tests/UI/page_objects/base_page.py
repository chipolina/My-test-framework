from typing import List

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    def element(self, locator: tuple) -> WebElement:
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент {locator} не видно на странице")

    def elements(self, locator: tuple) -> List[WebElement]:
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элементы {locator} не видны на странице")

    def check_len_elements(self, locator, number):
        assert len(self.elements(locator)) == number, f"Number of {len(self.elements(locator))} doesn't equal {number}"

    def check_element_text(self, locator, text):
        assert self.element(locator).text == text, f"Text of {self.element(locator)} doesn't equal {text}"
