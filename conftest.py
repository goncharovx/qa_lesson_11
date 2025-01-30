import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selene import Browser, Config
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager

if not os.path.exists(".env"):
    raise FileNotFoundError("Файл .env не найден в рабочей директории")

load_dotenv()


@pytest.fixture(scope="session")
def setup_browser():
    options = Options()

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    if not selenoid_url or selenoid_url.lower() in ["none", ""]:
        raise ValueError(f"Переменная SELENOID_URL не задана! Текущее значение: {selenoid_url}")

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.set_capability("selenoid:options", selenoid_capabilities)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser = Browser(Config(driver=driver))
    yield browser
    driver.quit()