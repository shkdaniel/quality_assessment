import pytest
import os
import tempfile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def init_driver(request):

    web_driver = None

    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def init_driver_profiles(request):

    web_driver = None

    if request.param == 'firefox':
        if not os.path.exists('firefox-data'):
            os.makedirs('firefox-data')
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-profile")
        firefox_options.add_argument('firefox-data')
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)

    if request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    request.cls.driver = web_driver
    yield
    web_driver.close()
