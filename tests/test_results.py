from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.homePage import homePage
from pages.resultsPage import resultsPage

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.results
def test_validateTheresultsUI(page:Page, navigateToAmazon):
    homePageObj = homePage(page)
    homePageObj.fillSerachBox()
    homePageObj.clickOnSeacrhBtn()
    resultsPageObj = resultsPage(page)
    resultsPageObj.validateTehVisibilityOdResultsText()
    expect(page).to_have_title("Amazon.in : iphone")
