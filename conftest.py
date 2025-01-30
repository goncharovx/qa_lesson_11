import os

import pytest
from dotenv import load_dotenv
from selene import Config, Browser, browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import attach

if not os.path.exists(".env"):
    raise FileNotFoundError("Файл .env не найден в рабочей директории")

# load_dotenv()


# @pytest.fixture(scope="session")
# def setup_browser():
#     options = Options()
#
#     selenoid_login = os.getenv("SELENOID_LOGIN")
#     selenoid_pass = os.getenv("SELENOID_PASS")
#     selenoid_url = os.getenv("SELENOID_URL")
#
#     if not selenoid_url or selenoid_url.lower() in ["none", ""]:
#         raise ValueError(f"Переменная SELENOID_URL не задана! Текущее значение: {selenoid_url}")
#
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "125.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#
#     options.set_capability("selenoid:options", selenoid_capabilities)
#
#     service = Service(ChromeDriverManager().install())
#
#     driver = webdriver.Remote(
#         command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
#         options=options
#     )
#
#     browser = Browser(Config(driver=driver))
#     yield browser
#     driver.quit()


DEFAULT_BROWSER_VERSION = "126.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION,
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
        keep_alive=True
    )

    browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()

    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--ignore-certificate-errors')
    browser.config.driver_options = driver_options

    browser.config.window_width = 1280
    browser.config.window_height = 724

    browser.config.base_url = 'https://demoqa.com'

    yield browser

    attach.add_screenshot(browser)  # Все методы должны работать с browser
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()