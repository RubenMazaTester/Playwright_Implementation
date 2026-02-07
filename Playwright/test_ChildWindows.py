import time

from playwright.sync_api import Page


#With this test function, we are going to handle child windows
def test_childWindowsNavigation(page: Page):

    #as usual, we get a url
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    """in this test we expect a popup to appear when we click on the link. We can use
    a method to let playwright know that there might be a pop up and return it as 
    new page to interact with"""
    with page.expect_popup() as newPageData:
        """we implemented this method to keep executing as usual but when a popup
        executes, the object we made is going to be active, so, we can
        """
        #step1, no popup, so no new object created
        #step2, no popúp, so no new object created

    #step3 in this step, we will click the popup, so the object will be used
        # we locate a link that will open the other tap
        page.locator(".blinkingText").click()  # We use this unique CSS to save time writting more text
        # page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()

        """now, our object is made, this object value makes playwright aware of the popup
        but, we have to use this value to create our new page """
        childPage=newPageData.value
        """now, we can use this childPage as a driver to interact as long as the
        the code is wrapped inside the method"""

        #we will make an assertion by splitting a string, to ensure a specific text is present
        redtext= childPage.locator(".red").text_content()

        #at this point, we see that we can print the whole text but, I want to take the email
        #to make an assertion with it, we can use basic python for this
        print(redtext)

        firstsplit= redtext.split("at")
        #we splitted our text by taking "at" as our reference, so, the string will now be
        #divided in 2 strings
        print(firstsplit[1])#now, we only show one string. but there´s text that we can trim

        secondsplit = firstsplit[1].split(" ")
        print(secondsplit[1])

        email= secondsplit[1]

        assert email=="mentor@rahulshettyacademy.com"



        #now, we are getting the text inside this locator, we can locate it easily by partial text
        text = childPage.get_by_text("Note").text_content()

        #after creating an object of it, we print the text to validate it
        print(text)







    time.sleep(3)