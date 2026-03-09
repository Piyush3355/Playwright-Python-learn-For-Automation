import pytest
from playwright.sync_api import sync_playwright

@ pytest.fixture
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
    login_page.wait_for_selector("text=Logged In Successfully")
    content = login_page.content()
    assert "Congratulations" in content

def test_invalid_login(login_page):
    login_page.fill("#username", "student")
    login_page.fill("#password", "Password123")
    login_page.click("#submit")
    login_page.wait_for_timeout(1500)
    content = login_page.content()
    assert "error" in content.lower()

    

        