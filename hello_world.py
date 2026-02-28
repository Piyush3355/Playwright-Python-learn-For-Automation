from playwright .sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.firefox.launch(headless=False)

    page = browser.new_page()

    page.goto("https://the-elefant-nextjs-web-v2.vercel.app/")

    page.wait_for_timeout(3000)

    browser.close()

    print("First test complete")

    