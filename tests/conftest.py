import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()

    # Настройки Selenoid
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "100.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    # Подключаемся к удалённому WebDriver (Selenoid)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    # Добавляем артефакты в Allure
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()