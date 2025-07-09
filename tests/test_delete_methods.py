from playwright.sync_api import Playwright
''''
API 9: DELETE To Verify Login
API URL: https://automationexercise.com/api/verifyLogin
Request Method: DELETE
Response Code: 405
Response Message: This request method is not supported.
'''
def test_delete_to_verify_login(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.delete("https://automationexercise.com/api/verifyLogin")
    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


''''
API 12: DELETE METHOD To Delete User Account
API URL: https://automationexercise.com/api/deleteAccount
Request Method: DELETE
Request Parameters: email, password
Response Code: 200
Response Message: Account deleted!
'''
def test_delete_delete_account(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.delete("https://automationexercise.com/api/deleteAccount",
                              form={
                                  "email": "petru@gmail",
                                  "password": "petrica"
                              })
    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"