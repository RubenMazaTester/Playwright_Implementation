import time

from playwright.sync_api import Playwright, expect

from Utils.ApiBase import APIutils


def test_e2ewebApi(playwright: Playwright):

    #This is a hard coded example of the login process
    """browser=playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")

    to start this test, we want to create an order through API requests exclusively,
    after that, we will validate everything through UI validatiom


    #we landed on the page, let´s login
    page.get_by_placeholder("email@example.com").fill("batman@hotmail.com")#user
    page.get_by_placeholder("enter your passsword").fill("@Batmanshetty1")#pass
    page.get_by_role("button",name="login").click()"""


    """now, we have already define the api utilities in another page od this project, we are 
    implementating page object model"""

    #I imported the class APIutils to use its methos

    #and we will make an object of it to use the class methods from the other file
    apiutils = APIutils()

    #Here we are logging in without even seeing the UI
    apiutils.getToken(playwright)

    """Then, we can create an order, because we need a token that is generated after log in
    because, the create order request needs an authorization token, we will add it as a header
    """
    orderid = apiutils.createOrder(playwright)
    print(orderid)







    """    orderID = apiutils.createOrder(playwright)
    print(orderID)
    #now we validate that order ID refreshed in the orders page
    page=apiutils.getToken(playwright)
    page.get_by_role("button",name="ORDERS").click()
    row= page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button",name="View").click()
    #expect(page.locator(".tagline"))to_contain_text("Thank you for Shopping With Us")
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()"""