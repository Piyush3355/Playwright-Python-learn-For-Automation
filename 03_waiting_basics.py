from playwright.sync_api import sync_playwright 

def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.wait_for_selector("#submit")

        page.fill("#username", "student")
        page.fill("#password", "Password123")
        
        page.click("#submit")

        page.wait_for_selector("text=Logged In Successfully", timeout=5000)

        page.screenshot(path="login_success.png")

        browser.close()

if __name__ == "__main__":
    main()