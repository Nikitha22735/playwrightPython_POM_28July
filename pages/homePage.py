import allure
from playwright.sync_api import sync_playwright, expect, Page

class homePage:
    def __init__(self, page):
        self.searchBarTxtbox = page.get_by_placeholder("Search Amazon.in")
        self.carticon = page.locator("#nav-cart-count")
        self.logo = page.locator("#nav-logo-sprites")
        self.searchBtn =  page.locator("#nav-search-submit-button")


    @allure.step("validateTheVisibilityOfSearchBar")
    def validateTheVisibilityOfSearchBar(self):
        expect(self.searchBarTxtbox).to_be_visible()

    @allure.step("validateTheVisibilityOfCartIcon")
    def validateTheVisibilityOfCartIcon(self):
        expect(self.carticon).to_be_visible()

    @allure.step("validateTheVisibilityOfAmazonLogo")
    def validateTheVisibilityOfAmazonLogo(self):
        expect(self.logo).not_to_be_visible()

    @allure.step("fillTheSearchBox")
    def fillSerachBox(self):
        self.searchBarTxtbox.fill("iphone")

    @allure.step("clickOnSearchButton")
    def clickOnSeacrhBtn(self):
        self.searchBtn.click()