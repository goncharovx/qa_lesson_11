import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    # Вызов добавленных вложений после выполнения тестов
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()