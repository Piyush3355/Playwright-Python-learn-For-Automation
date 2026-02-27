from playwright.sync_api import sync_playwright

with sync_playwright() as d:
    browser = d.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")


    page.fill("#username", "student")

    page.fill("#password", "Password123")

    page.click("#submit")

    page.wait_for_timeout(3000)
    
    page.screenshot(path="after_login.png")

    browser.close()

    print("vhai gai login!")