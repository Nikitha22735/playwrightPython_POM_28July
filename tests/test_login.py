from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import loginPage
from utils import jsonhandling


@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.regression
def test_validatePositiveLoginWithValidCredentials(page: Page, navigateToAmazon) -> None:
    
    # Initialize login page object
    loginPageObj = loginPage(page)
    
    # Step 1: Verify initial page title
    expected_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    expect(page).to_have_title(expected_title)
    
    # Step 2: Click on "Accounts & Lists" link from home screen
    loginPageObj.clickAccountsAndListsLink()
    
    # Step 3: Wait for authentication screen to load
    loginPageObj.validateEmailFieldVisible()
    
    # Step 4: Enter valid email address
    data = jsonhandling('testData\\creds.json')
    loginPageObj.enterEmailOrMobile(data["positiveCreds"]["email"])
    
    # Step 5: Click Continue button
    loginPageObj.clickContinueBtn()
    
    # Step 6: Verify password field is visible and enter password
    loginPageObj.validatePasswordFieldVisible()
    loginPageObj.enterPassword("Welcome@04")
    
    # Step 7: Click Sign In button
    loginPageObj.clickSignInBtn()
    
    # Step 8: Verify successful login by checking search box visibility
    loginPageObj.validateSearchBoxVisible()


# @pytest.mark.login
@pytest.mark.smoke
def test_validateLoginNavigationToAuthenticationScreen(page: Page, navigateToAmazon) -> None:

    
    # Initialize login page object
    loginPageObj = loginPage(page)
    
    # Step 1: Click on "Accounts & Lists" link
    loginPageObj.clickAccountsAndListsLink()
    
    # Step 2: Verify email field is visible on authentication screen
    loginPageObj.validateEmailFieldVisible()
