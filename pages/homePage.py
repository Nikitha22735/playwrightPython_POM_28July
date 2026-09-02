from playwright.sync_api import sync_playwright, expect, Page

class homePage:
    def __init__(self, page):
        self.searchBarTxtbox = page.get_by_placeholder("Search Amazon.in")
        self.carticon = page.locator("#nav-cart-count")
        self.logo = page.locator("#nav-logo-sprites")
        self.searchBtn =  page.locator("#nav-search-submit-button")


    def validateTheVisibilityOfSearchBar(self):
        expect(self.searchBarTxtbox).to_be_visible()

    def validateTheVisibilityOfCartIcon(self):
        expect(self.carticon).to_be_visible()

    def validateTheVisibilityOfAmazonLogo(self):
        expect( self.logo).to_be_visible()

    def fillSerachBox(self):
        self.searchBarTxtbox.fill("iphone")

    def clickOnSeacrhBtn(self):
        self.searchBtn.click()