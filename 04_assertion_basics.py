from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.fill("#username", "student")
        page.fill("#password", "Password123")
        page.click("#submit")

        page.wait_for_selector("text=Logged In Successfully")

        content = page.content()
        assert "Congratulations" in content, "Login did not succeed!"

        page.screenshot(path="04SS.png")
        browser.close()
        print("Assertion complete!")

if __name__ == "__main__":
    main()