from playwright.sync_api import Playwright

def test_put_to_products(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.put("https://automationexercise.com/api/productsList")
    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


''''
API 13: PUT METHOD To Update User Account
API URL: https://automationexercise.com/api/updateAccount
Request Method: PUT
Request Parameters: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
Response Code: 200
Response Message: User updated!'''

def test_put_to_update_user_account(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.put("https://automationexercise.com/api/updateAccount")
    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."