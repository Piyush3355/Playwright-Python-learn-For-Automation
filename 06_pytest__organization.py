# import pytest
# from playwright.sync_api import sync_playwright

# @ pytest.fixture
# def login_page():
#     with sync_playwright() as p:
#         browser = p.firefox.launch(headless=True)
#         page = browser.new_page()
#         page.goto("https://practicetestautomation.com/practice-test-login/")
#         yield page
#         browser.close()

# def test_valid_login(login_page):
#     login_page.fill("#username", "student")
#     login_page.fill("#password", "Password123")
#     login_page.click("#submit")
#     login_page.wait_for_selector("text=Logged In Successfully")
#     content = login_page.content()
#     assert "Congratulations" in content

# def test_invalid_login(login_page):
#     login_page.fill("#username", "student")
#     login_page.fill("#password", "Password123")
#     login_page.click("#submit")
#     login_page.wait_for_timeout(1500)
#     content = login_page.content()
#     assert "error" in content.lower()
        

from playwright.sync_api import sync_playwright

def check_media_devices():
    with sync_playwright() as p:
        # We use chromium here as it has better hardware permission flags
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Go to a site that tests webcam capabilities
        page.goto("https://webcamtests.com/")
        
        # Take a screenshot of the hardware detection area
        page.wait_for_timeout(3000) # Give it a moment to probe hardware
        page.screenshot(path="hardware_check.png")
        
        print("Check hardware_check.png to see if the browser detected your camera.")
        browser.close()

if __name__ == "__main__":
    check_media_devices()