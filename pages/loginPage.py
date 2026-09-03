from playwright.sync_api import expect, Page


class loginPage:
    """Page Object for Amazon Login Page"""

    def __init__(self, page: Page):
        self.page = page
        
        # Home screen elements
        self.accountsAndListsLink = page.get_by_role("link", name="Hello, sign in Account & Lists")
        
        # Authentication screen elements
        self.emailTextbox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.passwordTextbox = page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        
        # Post-login validation elements
        self.searchBox = page.get_by_role("searchbox", name="Search Amazon.in")

    # Home Screen Actions
    def clickAccountsAndListsLink(self):
        """Click on Accounts & Lists link from home screen"""
        self.accountsAndListsLink.click()

    # Authentication Screen Actions
    def enterEmailOrMobile(self, email: str):
        """Enter email or mobile number on authentication screen"""
        self.emailTextbox.click()
        self.emailTextbox.fill(email)

    def clickContinueBtn(self):
        """Click Continue button on authentication screen"""
        self.continueBtn.click()

    def enterPassword(self, password: str):
        """Enter password on authentication screen"""
        self.passwordTextbox.fill(password)

    def clickSignInBtn(self):
        """Click Sign In button to complete login"""
        self.signInBtn.click()

    # Validation Methods
    def validateSearchBoxVisible(self):
        """Validate that search box is visible (indicating successful login)"""
        expect(self.searchBox).to_be_visible()

    def validatePasswordFieldVisible(self):
        """Validate that password field is visible on authentication screen"""
        expect(self.passwordTextbox).to_be_visible()

    def validateEmailFieldVisible(self):
        """Validate that email field is visible on authentication screen"""
        expect(self.emailTextbox).to_be_visible()
