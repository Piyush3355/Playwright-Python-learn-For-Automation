import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    print("Setting up browser (fixture)")
    p = sync_playwright().start()
    browser = p.firefox.launch(headless=False)
    yield browser
    print("Closing browser (fixture)")
    browser.close()
    p.stop()

@pytest.fixture
def login_page(browser):
    print("Creating new page and navigating to login")
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    yield page
    print("Closing page")
    page.close()

def test_valid_login(login_page):
    login_page.fill("#username", "student")
    login_page.fill("#password", "Password123")
    login_page.click("#submit")
    login_page.wait_for_selector("text=Logged In Successfully")
    content = login_page.content()
    assert "Congratulations" in content
    print("Valid login test passed")

def test_invalid_login(login_page):
    login_page.fill("#username", "student")
    login_page.fill("#password", "wrongpassword")
    login_page.click("#submit")
    login_page.wait_for_selector("text=Your password is invalid!")
    content = login_page.content()
    assert "invalid" in content.lower()
    print("Invalid login test passed")
