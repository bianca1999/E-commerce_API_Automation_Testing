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


