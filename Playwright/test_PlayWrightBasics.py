import time

from playwright.sync_api import Page

def test_playWrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context1 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://rahulshettyacademy.com")

#Chromium engine, headless and single context
def test_fasterWay(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_mainLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    page.get_by_role("combobox").select_option("consult")

    #page.get_by_label("terms").click()
    #we can also locate with css selectors
    page.locator("#terms").check()

    page.get_by_role("link", name="terms and conditions").click()

    page.get_by_role("button",name="Sign in").click()

    time.sleep(3)

#Let´s now try an example for when the label is not directly linked to the item we want
# to interact

def test_labelNotPresent(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
#if the interactable element is not wrapped inside the label, we can link it
#through it´s for attribute but, it is only in case that the input element
#has the for attribute text inside of it.

