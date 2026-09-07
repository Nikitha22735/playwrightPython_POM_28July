import allure
from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.fixture()
def navigateToAmazon(page: Page):
    page.goto("https://www.amazon.in/")
    countOfBtns = page.locator('//*[contains(text(),"Shopping")]').count()
    if countOfBtns>0:
        page.locator('//*[contains(text(),"Shopping")]').click()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(page.screenshot(),name="failedpage")


def pytest_sessionstart(session):
    
    with open("allure-results/environment.properties", "w") as f:
        f.write("regression build123\n")