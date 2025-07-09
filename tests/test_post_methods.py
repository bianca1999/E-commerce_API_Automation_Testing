import pytest
from playwright.sync_api import Playwright

def test_post_to_products(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/productsList")
    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


@pytest.mark.parametrize('product', ['top', 'jeans', 'dress'])
def test_post_to_search_products(playwright: Playwright, product):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/searchProduct",
                            form = {"search_product": product})

    data = response.json()

    assert data["responseCode"] == 200
    assert 'products' in data
    assert isinstance(data['products'], list)
    assert len(data['products']) > 0

    for product in data['products']:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product

'''
POST To Search Product without search_product parameter
API URL: https://automationexercise.com/api/searchProduct
Request Method: POST
Response Code: 400
Response Message: Bad request, search_product parameter is missing in POST request.
'''
def test_post_to_search_products_without_product(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/searchProduct")

    data = response.json()

    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."

'''
API 7: POST To Verify Login with valid details
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameters: email, password
Response Code: 200
Response Message: User exists!
'''
def test_post_verify_login_existing_user(playwright:Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/verifyLogin",
                            form={
                                "email": "bianca@gmail",
                                "password": "123456"
                            })
    data = response.json()

    assert data['responseCode'] == 200
    assert data['message'] == "User exists!"


''''
POST To Verify Login without email parameter
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameter: password
Response Code: 400
Response Message: Bad request, email or password parameter is missing in POST request.
'''
def test_post_verify_login_without_email(playwright:Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/verifyLogin")
    data = response.json()

    assert data['responseCode'] == 400
    assert data['message'] == "Bad request, email or password parameter is missing in POST request."

'''
API URL: https://automationexercise.com/api/verifyLogin
Request Method: POST
Request Parameters: email, password (invalid values)
Response Code: 404
Response Message: User not found!
'''
def test_post_verify_login_invalid_credentials(playwright:Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/verifyLogin",
                            form={
                                "email": "petru@gmail.com",
                                "password": "12345"
                            })
    data = response.json()

    assert data['responseCode'] == 404
    assert data['message'] == "User not found!"

''''
API 11: POST To Create/Register User Account
API URL: https://automationexercise.com/api/createAccount
Request Method: POST
Request Parameters: name, email, password, title (for example: Mr, Mrs, Miss), birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number
Response Code: 201
Response Message: User created!
'''
def test_post_register_user_account(playwright:Playwright):
    context = playwright.request.new_context()
    response = context.post("https://automationexercise.com/api/createAccount",
                            form={
                                "name": "Petru",
                                "email": "petru@gmail",
                                "password": "petrica",
                                "title": "Mr",
                                "birth_date": "19",
                                "birth_month": "6",
                                "birth_year": "1992",
                                "firstname": "Petru",
                                "lastname": "Schipor",
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

    assert data['responseCode'] == 201
    assert data['message'] == "User created!"