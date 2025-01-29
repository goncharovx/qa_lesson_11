import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def setup_browser():
    use_selenoid = True
    if use_selenoid:
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
    else:
        options = Options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    browser = Browser(Config(driver))
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if use_selenoid:
        attach.add_video(browser)

    browser.quit()