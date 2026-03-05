from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        page.wait_for_event(2000)
        page.screenshot(path="01.ss.png")
        browser.close()

        if __name__ == "__main__":
            main()