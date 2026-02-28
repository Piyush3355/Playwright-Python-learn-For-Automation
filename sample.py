from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto("https://exercism.org/tracks/python")

    page.wait_for_timeout(2000)

    page.screenshot(path="ss.png")

    browser.close()

    print("ss saved")
    