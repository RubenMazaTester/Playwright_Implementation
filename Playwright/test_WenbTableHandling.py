from playwright.sync_api import Page, expect

#Check the price of an item by handling a web table
"""We are about to handle a web table,so, this means that is a dynamic element, the items,
columns or rows can change at any time, so if we hard code this test, it can be outdated
quickly, we should make it as dynamic and versatile as possible

"""

def test_tableHandling(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #locate the table
    #wholetable = page.locator(".table")

    #now, we locate the prices column
    #columns = wholetable.locator("th")

    #there are several columns, so we can iterate through them to parse the date into al list
    for index in range(page.locator("th").count()):
       if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            colValue=index
            print(f"price column value is {colValue}")
            break



    #then the item row
    itemrow = page.locator("tr").filter(has_text="Wheat")

    #now, we want to extract the price column for this item and make an assertion
    expect(itemrow.locator("td").nth(colValue)).to_have_value("37")



    #filtereditem=itemrows.locator("td").text_content()






    """at this point, we defined the index for of the columns list, so, the prices
    are located in the rows of the column, that´s why we located the row of
    our desired item, so, we can make a variable to handle the itemrow object as a list
    and locate the price of our items thanks to the index we got from our for loop"""



