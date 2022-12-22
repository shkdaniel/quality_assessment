import os


class TestData:

    BASE_URL = 'https://www.hudl.com'
    USERNAME = os.environ.get('USER_NAME')
    PASSWORD = os.environ.get('PASSWORD')

    LOGIN_PAGE_TITLE = "Log In"
    HOME_PAGE_TITLE = "Home - Hudl"
    SIGNUP_TITLE = "Sign up for Hudl"
    LOGIN_ORGANIZATION_TITLE = "Log In with Organization - Hudl"
    LOGIN_ERROR_TEXT = "We didn't recognize that email and/or password."
    LOGIN_HELP_TEXT = "Login Help"
    MAIN_TITLE = "Hudl • Tools to help every team, coach and athlete improve"
    LOGIN_ERROR_ORGANIZATION_TEXT = "This account can't log in with an organization yet. Please log in using your email and password."

    TIMEOUT = 10



