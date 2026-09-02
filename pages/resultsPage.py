from playwright.sync_api import sync_playwright, expect, Page

class resultsPage:
    def __init__(self, page):
        self.ResultsText = page.locator("//h2[text()='Results']")

    def validateTehVisibilityOdResultsText(self):
        expect(self.ResultsText).to_be_visible()