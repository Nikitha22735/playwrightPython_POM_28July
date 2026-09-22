
import json

from playwright.sync_api import sync_playwright, expect, Page
import pytest
import urllib
capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 149,
    'LT:Options': {
        'platform': 'Windows 10',
        'build': 'Playwright Python Build 28 July',
        'name': 'Playwright Python Test',
        'user': 'nikithathripuram',
        'accessKey': 'LT_mdwSuSZ2SrRa7ZX9fI8nFWpCeXDK0COkVnrNl5pQGL8Wcuo',
        'network': True,
        'video': True,
        'console': True,
        'tunnel': False,  # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}


def test_geoLocation():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.launch(headless=False)
        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url)
        context = browser.new_context(geolocation={"latitude":36.778259,"longitude":-119.417931},permissions=["geolocation"])
        # context.set_geolocation()
        page = context.new_page()
        page.goto('https://browserleaks.com/geo')
        page.wait_for_timeout(5000)
