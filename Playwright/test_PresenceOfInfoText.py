#In this file, we are going to test the autowait feature on playwright
#This is specially useful because you don´t have to write a waiting function explicitely
#While in selenium, you have to do it manually, selenium doesn´t have an auto wait feature

from playwright.sync_api import Page, expect


#This is the expected text Incorrect username/password.


def test_infoTextAssert(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")

    page.get_by_role("combobox").select_option("consult")

    page.get_by_label("terms").click()

    page.get_by_role("link", name="terms and conditions").click()

    page.get_by_role("button",name="Sign in").click()

#Playwright does have methods to assert elements with the autowait
#It helps us te reduce the lines of code
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()