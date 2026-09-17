from playwright.sync_api import sync_playwright, expect, Page
import pytest

# @pytest.mark.av
def test_responsive():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width':1000,'height':400})
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        page.wait_for_timeout(5000)


# @pytest.mark.av
def test_mobile():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(**playwright.devices['iPhone XR'])
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        page.wait_for_timeout(5000)

# @pytest.mark.av
def test_geoLocation():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(geolocation={"latitude":36.778259,"longitude":-119.417931},permissions=["geolocation"])
        # context.set_geolocation()
        page = context.new_page()
        page.goto('https://browserleaks.com/geo')
        page.wait_for_timeout(5000)


# @pytest.mark.av
def test_offlinemode():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        page.wait_for_timeout(5000)
        context.set_offline(True)
        page.get_by_text('Udemy Courses').click()
        page.wait_for_timeout(5000)



@pytest.mark.av
def test_screenShots():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://testautomationpractice.blogspot.com/')
        # page.screenshot(path="screenshots/img1.png")
        # page.screenshot(path="screenshots/img2.png",full_page=True)
        # page.get_by_text("START").screenshot(path="screenshots/img3.png")
        page.locator('//input[@id="name"]/parent::div').screenshot(path="screenshots/img4.png")
