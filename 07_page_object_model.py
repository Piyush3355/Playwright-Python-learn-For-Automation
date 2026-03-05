from playwright.sync_api import sync_playwright

class loginpage:
    def __init__(self, page):
        self.page = page    
        self.username = "username"
        self.password = "password"
        self.submit = "submit"

    def goto(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")
        self.page.wait_for_timeout(500)


    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.submit)
        self.page.wait_for_selector(1500)

def test_login_with_pom():
    with sync_playwright() as p:
     browser = p.firefox.launch(headless=True)
     page = browser.new_page()
     login_page = loginpage(page)
     login_page.goto()
     login_page.login("student", "Password123")
     assert "Congratulations" in page.text_content()
     browser.close()
     print("Login with pom complete")

     if __name__ == "__main__":
         test_login_with_pom


