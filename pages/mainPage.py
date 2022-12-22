from pages.basePage import BasePage
from config.config import TestData


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/')

    def get_main_title(self, title):
        return self.get_title(title)
