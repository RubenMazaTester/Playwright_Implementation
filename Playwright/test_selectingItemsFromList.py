import time


from playwright.sync_api import Page, expect


#We use the param page because we are going to launch chromium
def test_selectItems(page: Page):

    #we reach the url
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    #we fill the log in data
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    # Here, we select an specific option from the combobox
    page.get_by_role("combobox").select_option("consult")

    # we click on the checkbox to check it
    page.get_by_label("terms").click()

    # we sign in by clicking the button
    page.get_by_role("button", name="Sign in").click()

    """in these next 2 lines we located the items that we want, then use the filter method
    to return only the items that have the defined text
    """
    blackberry = page.locator("app-card").filter(has_text="Blackberry")
    samsung = page.locator("app-card").filter(has_text="Samsung Note 8")

    """now that we filtered each item by its block, in the next 2 lines we click 
    on their add button"""
    blackberry.get_by_role("button").click()
    samsung.get_by_role("button").click()

    # we click on the checkout button that it located by its own descriptive text
    page.get_by_text("Checkout").click()

    """in the checkout page, we select all the elements that this css locator returns,
    we returned all of the added items
    """
    items = page.locator(".media-body")

    """we located all of the items that were added, now we make an assertion
    to make sure there are 2 items in the cart"""
    expect(items).to_have_count(2)

    """this is a time pause to verify exactly how the browser is being automated
    for theses tests, it is not advised to use in a work script"""
    time.sleep(4)
