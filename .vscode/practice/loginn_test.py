import pytest
from playwright.sync_api import sync_playwright

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.p = sync_playwright().start()
        self.browser = self.p.firefox.launch(headless=False)
        self.page = self.browser.new_page()
        yield
        self.browser.close()
        self.p.stop()

    def test_valid_login(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

        self.page.fill("#username", "student")
        self.page.fill("#password", "Password123")
        self.page.click("#submit")

        self.page.locator(".post-title").wait_for()

        page_text = self.page.text_content("body")
        assert "Congratulations" in page_text
        assert "Logged In Successfully" in page_text

    def test_invalid_login(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

        self.page.fill("#username", "student")
        self.page.fill("#password", "Wrongpass")
        self.page.click("#submit")

        page_text = self.page.text_content("body").lower()
        assert "error" in page_text or "invalid" in page_text

    def test_empty_username(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

        self.page.fill("#password", "Password123")
        self.page.click("#submit")

        page_text = self.page.text_content("body").lower()
        assert "error" in page_text or "required" in page_text
