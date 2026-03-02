"""
Multiple Login Tests with Playwright
Learning Goal: Write multiple test cases in one file
Testing different login scenarios
"""

from playwright.sync_api import sync_playwright


def test_valid_login():
    """Test 1: Login with correct credentials"""
    print("\n" + "=" * 50)
    print("TEST 1: Valid Login")
    print("=" * 50)
    
    with sync_playwright() as p:
        # Launch Firefox browser
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to login page
        print("\n1️⃣  Navigating to login page...")
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.wait_for_timeout(1000)
        
        # Fill username
        print("2️⃣  Filling username...")
        page.fill("#username", "student")
        assert page.input_value("#username") == "student"
        print("   ✅ Username filled correctly")
        
        # Fill password
        print("3️⃣  Filling password...")
        page.fill("#password", "Password123")
        assert page.input_value("#password") == "Password123"
        print("   ✅ Password filled correctly")
        
        # Click login button
        print("4️⃣  Clicking login button...")
        page.click("#submit")
        
        # Wait for success message
        print("5️⃣  Waiting for success message...")
        page.wait_for_timeout(2000)
        
        # Verify login was successful
        print("6️⃣  Verifying login success...")
        assert "Congratulations" in page.text_content()
        print("   ✅ Success message found!")
        
        # Take screenshot
        page.screenshot(path="test1_valid_login_success.png")
        print("   📸 Screenshot saved: test1_valid_login_success.png")
        
        browser.close()
        print("\n✅ TEST 1 PASSED!\n")


def test_invalid_password():
    """Test 2: Login with invalid password"""
    print("\n" + "=" * 50)
    print("TEST 2: Invalid Password")
    print("=" * 50)
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to login page
        print("\n1️⃣  Navigating to login page...")
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.wait_for_timeout(1000)
        
        # Fill username
        print("2️⃣  Filling username...")
        page.fill("#username", "student")
        
        # Fill wrong password
        print("3️⃣  Filling wrong password...")
        page.fill("#password", "WrongPassword123")
        
        # Click login button
        print("4️⃣  Clicking login button...")
        page.click("#submit")
        
        # Wait for error message
        print("5️⃣  Waiting for error message...")
        page.wait_for_timeout(2000)
        
        # Verify error message appears
        print("6️⃣  Verifying error message...")
        page_text = page.text_content()
        assert "error" in page_text.lower() or "invalid" in page_text.lower()
        print("   ✅ Error message found!")
        
        # Take screenshot
        page.screenshot(path="test2_invalid_password.png")
        print("   📸 Screenshot saved: test2_invalid_password.png")
        
        browser.close()
        print("\n✅ TEST 2 PASSED!\n")


def test_empty_username():
    """Test 3: Login with empty username"""
    print("\n" + "=" * 50)
    print("TEST 3: Empty Username")
    print("=" * 50)
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to login page
        print("\n1️⃣  Navigating to login page...")
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.wait_for_timeout(1000)
        
        # Leave username empty
        print("2️⃣  Leaving username empty...")
        
        # Fill password
        print("3️⃣  Filling password...")
        page.fill("#password", "Password123")
        
        # Click login button
        print("4️⃣  Clicking login button...")
        page.click("#submit")
        
        # Wait for validation error
        print("5️⃣  Waiting for validation error...")
        page.wait_for_timeout(2000)
        
        # Verify error appears
        print("6️⃣  Verifying validation error...")
        page_text = page.text_content("body")
        assert "error" in page_text.lower() or "required" in page_text.lower()
        print("   ✅ Validation error found!")
        
        # Take screenshot
        page.screenshot(path="test3_empty_username.png")
        print("   📸 Screenshot saved: test3_empty_username.png")
        
        browser.close()
        print("\n✅ TEST 3 PASSED!\n")


def test_empty_password():
    """Test 4: Login with empty password"""
    print("\n" + "=" * 50)
    print("TEST 4: Empty Password")
    print("=" * 50)
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to login page
        print("\n1️⃣  Navigating to login page...")
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.wait_for_timeout(1000)
        
        # Fill username
        print("2️⃣  Filling username...")
        page.fill("#username", "student")
        
        # Leave password empty
        print("3️⃣  Leaving password empty...")
        
        # Click login button
        print("4️⃣  Clicking login button...")
        page.click("#submit")
        
        # Wait for validation error
        print("5️⃣  Waiting for validation error...")
        page.wait_for_timeout(2000)
        
        # Verify error appears
        print("6️⃣  Verifying validation error...")
        page_text = page.text_content()
        assert "error" in page_text.lower() or "required" in page_text.lower()
        print("   ✅ Validation error found!")
        
        # Take screenshot
        page.screenshot(path="test4_empty_password.png")
        print("   📸 Screenshot saved: test4_empty_password.png")
        
        browser.close()
        print("\n✅ TEST 4 PASSED!\n")


def test_both_fields_empty():
    """Test 5: Login with both fields empty"""
    print("\n" + "=" * 50)
    print("TEST 5: Both Fields Empty")
    print("=" * 50)
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to login page
        print("\n1️⃣  Navigating to login page...")
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.wait_for_timeout(1000)
        
        # Leave both fields empty
        print("2️⃣  Leaving both fields empty...")
        
        # Click login button
        print("3️⃣  Clicking login button...")
        page.click("#submit")
        
        # Wait for validation error
        print("4️⃣  Waiting for validation error...")
        page.wait_for_timeout(2000)
        
        # Verify error appears
        print("5️⃣  Verifying validation error...")
        page_text = page.text_content()
        assert "error" in page_text.lower() or "required" in page_text.lower()
        print("   ✅ Validation error found!")
        
        # Take screenshot
        page.screenshot(path="test5_both_empty.png")
        print("   📸 Screenshot saved: test5_both_empty.png")
        
        browser.close()
        print("\n✅ TEST 5 PASSED!\n")


def main():
    """Run all tests"""
    print("\n" + "🧪 STARTING ALL TESTS ".center(50, "="))
    
    try:
        # Run each test
        test_valid_login()
        test_invalid_password()
        test_empty_username()
        test_empty_password()
        test_both_fields_empty()
        
        # Print summary
        print("\n" + "=" * 50)
        print("🎉 ALL 5 TESTS PASSED!")
        print("=" * 50)
        print("\nScreenshots saved:")
        print("  - test1_valid_login_success.png")
        print("  - test2_invalid_password.png")
        print("  - test3_empty_username.png")
        print("  - test4_empty_password.png")
        print("  - test5_both_empty.png")
        print("\n✨ Excellent progress!\n")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR OCCURRED: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)