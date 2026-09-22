import allure
from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.fixture()
def navigateToAmazon(page: Page):
    page.goto("https://www.amazon.in/")
    # countOfBtns = page.locator('//*[contains(text(),"Shopping")]').count()
    # if countOfBtns>0:
    #     page.locator('//*[contains(text(),"Shopping")]').click()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(page.screenshot(),name="failedpage")


# def pytest_sessionstart(session):
    
#     with open("allure-results/environment.properties", "w") as f:
#         f.write("regression build123\n")



# @pytest.fixture()
# def page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(viewport={'width':1000,'height':400})
#         page = context.new_page()
#         yield page

# @pytest.fixture()
# def pageLambda():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(viewport={'width':1000,'height':400})
#         page = context.new_page()
#         yield page


# ===============
@pytest.fixture(scope="session")
def cookies():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_role("textbox", name="Username").fill("Admin")
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
        context.storage_state(path='testData\\auth.json')

# @pytest.mark.av
# def page(browser):
#     # with sync_playwright() as playwright:
#     #     browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(storage_state='testData\\auth.json')
#         page = context.new_page()
#         yield page