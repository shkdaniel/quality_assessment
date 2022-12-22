import time
import pytest
from selenium.common.exceptions import TimeoutException
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.signupPage import SignupPage
from pages.mainPage import MainPage
from pages.loginOrgPage import LoginOrgPage
from config.config import TestData


@pytest.mark.usefixtures('init_driver')
class TestLogin:

    def test_signup_link_visible(self):
        """
        Positive test :: Verify if Sign up link is visible
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_signup_link_exists()

    def test_signup_link_clickable(self):
        """
        Positive test :: Verify if Sign up link is clickable
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_signup_link()
        self.signupPage = SignupPage(self.driver)
        assert self.signupPage.get_signup_title(TestData.SIGNUP_TITLE) == TestData.SIGNUP_TITLE

    def test_hudl_logo_visible(self):
        """
        Positive test :: Verify if Hudl logo is visible
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_hudl_logo_exists()

    def test_hudl_logo_clickable(self):
        """
        Positive test :: Verify if Hudl logo is clickable
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_hudl_logo()
        time.sleep(3)
        self.mainPage = MainPage(self.driver)
        assert self.mainPage.get_main_title(TestData.MAIN_TITLE) == TestData.MAIN_TITLE

    def test_back_icon_visible(self):
        """
        Positive test :: Verify if Back icon is visible
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_back_icon_exists()

    def test_back_icon_clickable(self):
        """
        Positive test :: Verify if Back icon is clickable
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_back_icon()
        time.sleep(3)
        self.mainPage = MainPage(self.driver)
        assert self.mainPage.get_main_title(TestData.MAIN_TITLE) == TestData.MAIN_TITLE

    def test_need_help_link_visible(self):
        """
        Positive test :: Verify if Need help? link is visible
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_help_link_exists()

    def test_need_help_link_clickable(self):
        """
        Positive test :: Verify if Need help? link is clickable
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_help_link()
        assert TestData.LOGIN_HELP_TEXT in self.loginPage.get_login_help_text()

    def test_login_page_title(self):
        """
        Positive test :: Verify Login page title
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.get_login_title(TestData.LOGIN_PAGE_TITLE) == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        """
        Positive test :: Verify if a user will be able to log in with a valid username and valid password
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        time.sleep(1)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_home_title(TestData.HOME_PAGE_TITLE) == TestData.HOME_PAGE_TITLE

    def test_login_invalid_password(self):
        """
        Negative test :: Verify if a user cannot log in with a valid username and an invalid password
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, '@!#$$%^&8899')
        assert TestData.LOGIN_ERROR_TEXT in self.loginPage.get_error_text()

    def test_login_blank_credentials(self):
        """
        Negative test :: Verify if a user cannot log in with blank credentials
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login('', '')
        assert TestData.LOGIN_ERROR_TEXT in self.loginPage.get_error_text()

    def test_login_organization_visible(self):
        """
        Positive test :: Verify if Organization login link is visible
        """
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_login_organization_link_exists()

    def test_login_organization_clickable(self):
        """
        Positive test :: Verify if Organization login link is clickable
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_login_organization_link()
        self.loginOrgPage = LoginOrgPage(self.driver)
        assert self.loginOrgPage.get_login_organization_title(TestData.LOGIN_ORGANIZATION_TITLE) == TestData.LOGIN_ORGANIZATION_TITLE

    def test_login_organization_with_private_email(self):
        """
        Negative test :: Verify if a user cannot log in with private email in organization account
        """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.click_login_organization_link()
        self.loginOrgPage = LoginOrgPage(self.driver)
        self.loginOrgPage.do_login_organization(TestData.USERNAME)
        assert TestData.LOGIN_ERROR_ORGANIZATION_TEXT in self.loginPage.get_error_text()


@pytest.mark.usefixtures('init_driver_profiles')
class TestLoginRem:
    def test_login_unchecked_remember_me(self):
        """
        Positive test :: Verify the "Remember me" is unchecked
        """
        try:
            self.loginPage = LoginPage(self.driver)
            assert not self.loginPage.is_selected_remember_me_checkbox()
        finally:
            self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
            time.sleep(1)

    def test_verify_unchecked_remember_me(self):
        """
        Positive test :: Verify the "Remember me" functionality when unchecked
        Dependency on the previous test "test_login_unchecked_remember_me"
        """
        try:
            self.homePage = HomePage(self.driver)
            assert self.homePage.get_home_title(TestData.HOME_PAGE_TITLE) != TestData.HOME_PAGE_TITLE
        except TimeoutException:
            assert True

    def test_login_checked_remember_me(self):
        """
        Positive test :: Verify the "Remember me" is checked
        """
        try:
            self.loginPage = LoginPage(self.driver)
            self.loginPage.click_remember_me_checkbox()
            time.sleep(3)
            assert self.loginPage.is_selected_remember_me_checkbox()
        finally:
            self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
            time.sleep(3)

    def test_verify_checked_remember_me(self):
        """
        Positive test :: Verify the "Remember me" functionality when checked
        Dependency on the previous test "test_login_checked_remember_me"
        """
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_home_title(TestData.HOME_PAGE_TITLE) == TestData.HOME_PAGE_TITLE
