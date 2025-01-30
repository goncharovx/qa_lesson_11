import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv

if not os.path.exists(".env"):
    raise FileNotFoundError("Файл .env не найден в рабочей директории")

load_dotenv()

print("SELENOID_LOGIN:", os.getenv("SELENOID_LOGIN"))
print("SELENOID_PASS:", os.getenv("SELENOID_PASS"))
print("SELENOID_URL:", os.getenv("SELENOID_URL"))

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
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    options.set_capability("selenoid:options", selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser = Browser(Config(driver=driver))
    browser.config.driver = driver

    yield browser
    driver.quit()
