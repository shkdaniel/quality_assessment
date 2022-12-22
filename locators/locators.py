from selenium.webdriver.common.by import By


class Locators:

    """Login Page Locators"""
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "logIn")
    EMAIL_ORGANIZATION = (By.NAME, 'username')
    LOGIN_BUTTON_ORGANIZATION = (By.CSS_SELECTOR, "button[data-qa-id='log-in-with-sso']")
    REMEMBER_ME_LABEL = (By.CSS_SELECTOR, "label[data-qa-id='remember-me-checkbox-label']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//div[contains(@class, 'check-item')]")
    NEED_HELP_LINK = (By.LINK_TEXT, "Need help?")
    LOGIN_ORGANIZATION_LINK = (By.LINK_TEXT, "Log In with an Organization")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    BACK_ICON = (By.XPATH, "//a[contains(@class, 'backIcon')]")
    LOGIN_ERROR = (By.CSS_SELECTOR, "p[data-qa-id='error-display']")
    LOGIN_HELP = (By.CSS_SELECTOR, "h2[data-qa-id='login-help-headline']")
    HUDL_LOGO = (By.XPATH, "//a[contains(@class, 'hudlLogo')]")
    HUDL_LOGO_IMG = (By.CSS_SELECTOR, "svg[data-qa-id='hudl-logo']")

    """Home Page Locators"""
