import playwright
from playwright.sync_api import Playwright

loginPayload = {"userEmail": "batman@hotmail.com", "userPassword": "@Batmanshetty1"}

requesPayload={"orders": [{"country": 'Guatemala', "productOrderedId": '6960ea76c941646b7a8b3dd5'}]}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTg5MmRlZGRjNDBiNDhmMTJjN2Q4OTIiLCJ1c2VyRW1haWwiOiJiYXRtYW5AaG90bWFpbC5jb20iLCJ1c2VyTW9iaWxlIjoxMjM0NTY3ODkxLCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzcwNTk4NjUxLCJleHAiOjE4MDIxNTYyNTF9.PhsdmgONvji7PcGOK80kPoYMpzZuo1VThOqBHS_hU9g"

class APIutils:

    def getToken(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        loginresponse = api_request_context.post("https://rahulshettyacademy.com/api/ecom/auth/login", data=loginPayload)

        assert loginresponse.ok
        print(loginresponse.json())
        responseBody = loginresponse.json()
        return responseBody["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context= playwright.request.new_context(base_url = "https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order", data=requesPayload,
                                 headers={"Authorization" : token , "content-type" : "application/json"})
        responseID = response.json()
        print(responseID)

        return responseID["orders"][0]




