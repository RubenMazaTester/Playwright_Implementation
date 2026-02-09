import json

import pytest
from playwright.sync_api import Page

with open("Daya/DataForTests") as f:
    test_data = json.load(f)
    test_data_list=test_data["user_credentials"]


@pytest.mark.parameterize
def loginPage(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill()