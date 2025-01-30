import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


# @pytest.fixture(scope='function')
# def setup_browser(request):
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "126.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True,
#         }
#     }
#
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=options
#     )
#     browser = Browser(Config(driver=driver))
#     yield browser
#
#     browser.quit()

@pytest.fixture(scope='function')
def setup_browser():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        },
    }
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities
    )
    browser = Browser(Config(driver=driver))
    yield browser
    browser.quit()