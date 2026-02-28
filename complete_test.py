from playwright.sync_api import sync_playwright

def test_login_and_purchase():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        print("Opening website")
        page.goto("https://practicetestautomation.com/practice-test-login/")

        print("Entering username")
        page.fill("#username", "student")

        print("Entering password")
        page.fill("#password", "Password123")

        print("Clicking login button")
        page.click("#submit")

        print("Waiting for success message")
        page.wait_for_selector("text=Congratulations")

        print("Verifying login")
        page_text = page.text_content("body")

        assert "Congratulations" in page_text
        assert "Logged In Successfully" in page_text

        page.screenshot(path="login_success.png")
        print("Screenshot saved")

        browser.close()
        print("Test complete")


if __name__ == "__main__":
    test_login_and_purchase()
