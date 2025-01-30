import os

import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.get_screenshot_as_png()
    allure.attach(png, name="screenshot", attachment_type=AttachmentType.PNG)


def add_logs(browser):
    logs = "".join(f"{entry}\n" for entry in browser.get_log("browser"))
    allure.attach(logs, name="browser_logs", attachment_type=AttachmentType.TEXT)


def add_html(browser):
    html = browser.page_source
    allure.attach(html, name="page_source", attachment_type=AttachmentType.HTML)


def add_video(browser):
    video_url = f"https://{os.getenv('SELENOID_URL')}/video/{browser.session_id}.mp4"
    html = f"<video width='100%' height='100%' controls autoplay><source src='{video_url}' type='video/mp4'></video>"
    allure.attach(html, name="video", attachment_type=AttachmentType.HTML)
