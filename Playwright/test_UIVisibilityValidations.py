import time

from playwright.sync_api import Page, expect


def test_UiVisibility(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    """for this test, we are going to use the locator getbyplaceholder, this locator helps to
    validate UI visibility changes using built-in assertions like to_be_visible() 
    and to_be_hidden() without relying on CSS selectors or hard waits.
    """
    #page.get_by_placeholder("Hide/Show Example")

    """for this test, we are going to test a element that can hidden or showed by 
    clicking 2 buttons, we can make an assertion to validate the visibility changes """
    #this is our first assertion to validate the element visibilty
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    """now, we are going to hide the element by clicking the hide button, so we need
    to locate the button an click it"""
    page.get_by_role("button", name="Hide").click()

    #validating that the element is hidden
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #In the same page, we can test JavaScript popups, playwright has methods to do it
    """to handle Js popups, we can do it similarly to the child windows, we  setup
    a method to make our code expect a Js popup and how to handle it"""
    page.on("dialog", lambda dialog:dialog.accept())
    """the method "on" requires 2 args, the event and the function to perform
    but, we can use lambda to make a single line function, we save time
    because we don´t need to define it"""

    #we locate the popup button
    page.locator("#confirmbtn").click()

