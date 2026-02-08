import time

from playwright.sync_api import Page, expect

"""for this test, we are going to handle web frames, this is similar to Js popups
since we can´t interact with it directly"""
def test_frameHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    #locate the frame element with the frame locator method and create a driver object
    pageframe= page.frame("iframe-name")
    pageframe.get_by_role("link", name ="All Access Plan").click()

    #now that we are handling the frame, we can make direct assertions
    #on the whole page
    expect(pageframe.locator("body")).to_contain_text("Unlimited Life time Access ")

    time.sleep(4)