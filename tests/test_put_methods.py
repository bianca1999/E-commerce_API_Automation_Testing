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

def test_put_update_user_account(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.put("https://automationexercise.com/api/updateAccount",
                           form={
                               "name": "Bianca",
                               "email": "bianca@gmail",
                               "password": "123456",
                               "title": "Mrs",
                               "birth_date": "19",
                               "birth_month": "6",
                               "birth_year": "1992",
                               "firstname": "Bianca",
                               "lastname": "Calancea",
                               "company": "WWS",
                               "address1": "South Perth",
                               "address2": "East Perth",
                               "country": "Australia",
                               "zipcode": "6151",
                               "state": "WA",
                               "city": "Perth",
                               "mobile_number": "12345678"
                           })

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"