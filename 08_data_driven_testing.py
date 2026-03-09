import pytest
from playwright.sync_api import sync_playwright

test_data =  [
    ("student", "Password123", True),
    ("student", "Wrongpassword", False),
    ("wronguser","Password", False),
    ("", "Password123", False), 
    ("", "", False),
]

@pytest.mark.parametrize("username,password,should_succeed", test_data)
def test_login_ddt(username, password, should_succeed):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.fill("#username", "student")
        page.fill("#password", "password")
        page.click("#submit")

        page.wait_for_timeout(1000)

        content = page.content()
        if should_succeed:
            assert "Congratulations" in content, f"Expected success, got failure for {username}/{password!r}"
        else:
            assert "error" in content.lower() or "invalid" in content in content.lower(), f" Expected error, got success for {username}/{password!r}"

            browser.close()