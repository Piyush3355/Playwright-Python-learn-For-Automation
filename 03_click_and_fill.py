from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")
   
    page.wait_for_timeout(1000)

    print("typing username")
    page.fill("#username", "student")

    print("typing pass")

    page.fill("#password", "Password123")

    print("typed pass")

    page.screenshot(path="before_login.png")

    print("clicking login button")

    page.click("#submit")

    page.wait_for_timeout(2000)

    page.screenshot(path="after_login.png")

    browser.close()

    print("login_test_complete")
    print("check 'before login.png' and 'after_login.png'")



