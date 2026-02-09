import time

from playwright.sync_api import Page


def test_mouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #when we entered the page, we need to locate the hover button
    page.locator("#mousehover").hover()

    #now we click an option
    page.get_by_role("link", name="Top").click()

    time.sleep(3)
