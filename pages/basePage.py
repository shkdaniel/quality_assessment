from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TestData


class BasePage:
    """
    The class is the parent for page classes
    The class contains generic methods for page classes
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        elem = WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return elem.text

    def is_visible(self, by_locator):
        elem = WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return bool(elem)

    def get_title(self, title):
        WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.title_is(title))
        return self.driver.title

    def is_selected(self, by_locator):
        elem = WebDriverWait(self.driver, TestData.TIMEOUT).until(EC.visibility_of_element_located(by_locator))
        return True if 'is-checked' in elem.get_attribute("class") else False

