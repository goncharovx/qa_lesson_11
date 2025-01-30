import os
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()  # Используем browser.driver для получения скриншота
    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png"
    )


def add_logs(browser):
    logs = "".join(f"{entry['level']}: {entry['message']}\n" for entry in browser.driver.get_log("browser"))  # Используем browser.driver
    allure.attach(
        logs,
        name="browser_logs",
        attachment_type=AttachmentType.TEXT,
        extension=".log"
    )


def add_html(browser):
    html = browser.driver.page_source  # Используем browser.driver для получения HTML-кода
    allure.attach(
        html,
        name="page_source",
        attachment_type=AttachmentType.HTML,
        extension=".html"
    )


def add_video(browser):
    video_url = f"https://{os.getenv('SELENOID_URL')}/video/{browser.driver.session_id}.mp4"
    html = f"<video width='100%' height='100%' controls autoplay><source src='{video_url}' type='video/mp4'></video>"
    allure.attach(html, name="video", attachment_type=AttachmentType.HTML)
