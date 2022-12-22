from pages.basePage import BasePage
from config.config import TestData


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/register/signup')

    def get_signup_title(self, title):
        return self.get_title(title)
