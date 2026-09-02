from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.fixture()
def navigateToAmazon(page: Page):
    page.goto("https://www.amazon.in/")
    countOfBtns = page.locator('//*[contains(text(),"Shopping")]').count()
    if countOfBtns>0:
        page.locator('//*[contains(text(),"Shopping")]').click()