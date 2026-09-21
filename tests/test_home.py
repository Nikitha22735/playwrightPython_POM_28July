import allure
from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import homePage
# Page, Context, Browser, Playwright

@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("home screen testcases")
def test_valdiatePageComponents(pageLambda: Page, navigateToAmazon):
    expect(pageLambda).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    expect(pageLambda).to_have_url("https://www.amazon.in/")

@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("home screen testcases")
def test_validateTheVisibilityofPageComponents(page:Page, navigateToAmazon):    
    homePageObj = homePage(page)
    homePageObj.validateTheVisibilityOfSearchBar()
    homePageObj.validateTheVisibilityOfCartIcon()
    homePageObj.validateTheVisibilityOfAmazonLogo()
   
    