from playwright.sync_api import Playwright
import json

def test_get_products(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.get("https://automationexercise.com/api/productsList")
    data = response.json()

    assert response.ok
    assert response.status == 200
    assert 'products' in data
    assert isinstance(data['products'], list)
    assert len(data['products']) > 0

    for product in data['products']:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product


'''
API URL: https://automationexercise.com/api/brandsList
Request Method: GET
Response Code: 200
Response JSON: All brands list
'''
def test_get_all_brands_list(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.get("https://automationexercise.com/api/brandsList")
    data = response.json()

    assert response.ok
    assert response.status == 200
    assert 'brands' in data
    assert isinstance(data['brands'], list)
    assert len(data['brands']) > 0

    for brand in data['brands']:
        assert 'id' in brand
        assert 'brand' in brand
