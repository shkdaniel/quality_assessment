from pages.basePage import BasePage
from config.config import TestData
from locators.locators import Locators


class LoginOrgPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/app/auth/login/organization')

    def get_login_organization_title(self, title):
        return self.get_title(title)

    def do_login_organization(self, username):
        self.do_send_keys(Locators.EMAIL_ORGANIZATION, username)
        self.do_click(Locators.LOGIN_BUTTON_ORGANIZATION)
