from playwright.sync_api import sync_playwright, expect, Page
import pytest

def test_example():
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

@pytest.mark.av
def test_example():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='testData\\auth.json')
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.wait_for_timeout(10000)