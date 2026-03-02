from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slow_mo=4000)
    page = browser.new_page()
    
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    page.wait_for_selector("text=Congratulations")
    
    page_text = page.content()

    print("page content after login")
    print(page_text)
    print("\n" + "="*50 + "\n")

    print("running assartions...")

    assert "Congratulations" in page_text, "Congratulations message not found!"
    print("test 1 pass : Congratulations not fount")

    assert "Logged In Successfully" in page_text, "Error: Login success text not found!"
    print("✅ Test 2 Passed: Success message confirmed.")

    assert "logged-in-successfully" in page.url, f"Error: URL is {page.url}"
    print("✅ Test 3 Passed: URL verified.")

    assert page.is_visible("text=Log out"), "Logout buttone not visible"
    print("test 4 passed: Logged out buttone is visible")

    page.screenshot(path="Login_success_verified.png")

    browser.close()
    print("\n ALL assertion passsed! test successfull")
