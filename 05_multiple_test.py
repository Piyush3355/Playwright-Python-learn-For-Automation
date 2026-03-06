from playwright.sync_api import sync_playwright

def test_valid_login():

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.fill("#username", "student")
        page.fill("#password", "Password123")
        page.click("#submit")

        page.wait_for_selector("text=Logged In Successfully")
        content = page.content()
        assert "Congratulations" in content, "valid login failed"
        browser.close()
        print("Valid login test passed")
def test_invalid_login():

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.fill("#username", "student")
        page.fill("#password", "wrongpass")
        page.click("#submit")

        content = page.content()

        assert "error" in content.lower(), "No error found no invalid login"
        browser.close()

        print("Invalid test passed")

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()        


        

