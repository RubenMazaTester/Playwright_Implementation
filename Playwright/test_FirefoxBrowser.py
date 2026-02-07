"""Here we can validate the launch of the firefox browser, if we want to launch firefox
we can´t use the shorcut page:Page as argument because, this shortcut launches only chromium
so, we have to use playwright:Playwright and create a context or page manually
"""
from playwright.sync_api import Playwright, expect


def test_loginFirefox(playwright:Playwright):
    fire = playwright.firefox.launch(headless=False)

    firecontext = fire.new_context()
    page= firecontext.new_page()

    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK21")

    page.get_by_role("combobox").select_option("consult")

    page.get_by_label("terms").click()

    page.get_by_role("link", name="terms and conditions").click()

    page.get_by_role("button", name="Sign in").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

#We made the same validation we did in chrome but now in firefox, works the same




