# """
# Learning Goal: Organize tests properly using pytest
# This is how professional testers write tests!

# Before running: pip install pytest
# """

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def login_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")
        yield page
        browser.close()

def test_valid_login(login_page):
    login_page.fill("#username", "student")
    login_page.fill("#password", "Password123")
    login_page.click("#submit")
    assert "Congratulations" in login_page.text_content("Body")

def test_invalid_login(login_page):
    login_page.fill("#username", "student")
    login_page.fill("#password", "Password")
    login_page.click("#submit")
    assert "error" in login_page.text_content("Body").lower()
