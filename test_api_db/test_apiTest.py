# Browser, Page, Context, playwright
from playwright.sync_api import sync_playwright
import pytest


def test_getAPI(playwright):
    #basic auth
    # context = playwright.request.new_context(http_credentials={"username":"admin","password":"admin"})
    context = playwright.request.new_context()
    responseToken= context.post("https://dummyjson.com/auth/login")
    responseTokenBody = responseToken.json()
    print(responseTokenBody["token"])
    # response=context.get("https://dummyjson.com/products?limit=5", headers={"Authorization":"Bearer 123456789"})
    response=context.get("https://dummyjson.com/products?limit=5", headers={"x-api-key":"123456789"})
    assert response.status == 200
    print(response)
    # print(response.json())
    responseBody = response.json()
    print(responseBody["products"][0]["title"])
    assert responseBody["products"][0]["title"]=="Essence Mascara Lash Princess"

@pytest.mark.api
def test_postApi(playwright):
    context = playwright.request.new_context()
    requestBody = {
            "title": "New Essence Mascara Lash Princess",
            "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
            "category": "beauty",
            "price": 9.99,
            "discountPercentage": 10.48,
            "rating": 2.56,
            "stock": 99,
            "tags": [
                "beauty",
                "mascara"
            ],
            "brand": "Essence",
            "sku": "BEA-ESS-ESS-001",
            "weight": 4,
            "dimensions": {
                "width": 15.14,
                "height": 13.08,
                "depth": 22.99
            },
            "warrantyInformation": "1 week warranty",
            "shippingInformation": "Ships in 3-5 business days",
            "availabilityStatus": "In Stock",
            "reviews": [
                {
                    "rating": 3,
                    "comment": "Would not recommend!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Eleanor Collins",
                    "reviewerEmail": "eleanor.collins@x.dummyjson.com"
                },
                {
                    "rating": 4,
                    "comment": "Very satisfied!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Lucas Gordon",
                    "reviewerEmail": "lucas.gordon@x.dummyjson.com"
                },
                {
                    "rating": 5,
                    "comment": "Highly impressed!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Eleanor Collins",
                    "reviewerEmail": "eleanor.collins@x.dummyjson.com"
                }
            ],
            "returnPolicy": "No return policy",
            "minimumOrderQuantity": 48,
            "meta": {
                "createdAt": "2025-10-09T14:47:01.588Z",
                "updatedAt": "2026-05-23T11:27:41.868Z",
                "barcode": "5784719087687",
                "qrCode": "https://cdn.dummyjson.com/public/qr-code.png"
            },
            "images": [
                "https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp"
            ],
            "thumbnail": "https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp"
        }
    response = context.post("https://dummyjson.com/products/add",headers={"x-api-key":"123456789"}, data=requestBody)
    assert response.status == 201
    # print(response.json())
    responseBody = response.json()
    print(responseBody["id"])


# def test_trad(page):
    # with sync_playwright() as playwright:
        # browser = playwright.chromium.launch()
        # context = browser.new_context()
        # page= context.new_page()


    