from pages.basePage import BasePage
from locators.locators import Locators
from config.config import TestData


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/login')

    def get_login_title(self, title):
        return self.get_title(title)

    def is_signup_link_exists(self):
        return self.is_visible(Locators.SIGNUP_LINK)

    def is_help_link_exists(self):
        return self.is_visible(Locators.NEED_HELP_LINK)

    def click_signup_link(self):
        self.do_click(Locators.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(Locators.EMAIL, username)
        self.do_send_keys(Locators.PASSWORD, password)
        self.do_click(Locators.LOGIN_BUTTON)

    def get_error_text(self):
        return self.get_text(Locators.LOGIN_ERROR)

    def click_help_link(self):
        self.do_click(Locators.NEED_HELP_LINK)

    def get_login_help_text(self):
        return self.get_text(Locators.LOGIN_HELP)

    def click_remember_me_checkbox(self):
        self.do_click(Locators.REMEMBER_ME_LABEL)

    def is_selected_remember_me_checkbox(self):
        return self.is_selected(Locators.REMEMBER_ME_CHECKBOX)

    def is_hudl_logo_exists(self):
        return self.is_visible(Locators.HUDL_LOGO_IMG)

    def click_hudl_logo(self):
        self.do_click(Locators.HUDL_LOGO)

    def is_back_icon_exists(self):
        return self.is_visible(Locators.BACK_ICON)

    def click_back_icon(self):
        self.do_click(Locators.BACK_ICON)

    def is_login_organization_link_exists(self):
        return  self.is_visible(Locators.LOGIN_ORGANIZATION_LINK)

    def click_login_organization_link(self):
        self.do_click(Locators.LOGIN_ORGANIZATION_LINK)
