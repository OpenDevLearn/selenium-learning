"""
Day 04 - Homework Exercise 3: Complete the Screenshot-on-Failure Pattern
==========================================================================
TASK: Fill in the blanks to create a test function that takes screenshots on failure.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def run_test(driver, test_name, test_func):
    """Run a test function and take a screenshot on failure."""
    try:
        print(f"Running: {test_name}...", end=" ")
        test_func(driver)
        print("✅ PASSED")
        return True
    except Exception as e:
        filepath = os.path.join(SCREENSHOT_DIR, f"{test_name}_FAILED.png")
        driver._____(_____)                             # 1. Save a screenshot
        print(f"❌ FAILED - {type(e).__name__}: {e}")
        print(f"   Screenshot: {filepath}")
        return False


def test_home_page(driver):
    """Verify home page loads correctly."""
    driver.get("http://localhost:5000")
    _____ = WebDriverWait(driver, 10).until(            # 2. Create a wait variable
        EC._____(                                        # 3. Expected condition for presence
            (By.ID, "page-title")
        )
    )
    assert "Selenium" in _____.text                      # 4. Check element text


def test_login_valid(driver):
    """Verify valid login works."""
    driver.get("http://localhost:5000/login")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password")._____("password123")  # 5. Method to type
    driver.find_element(By.ID, "login-btn")._____()              # 6. Method to click

    WebDriverWait(driver, 10).until(
        EC._____(_____)                                  # 7. Wait for URL to contain "dashboard"
    )


def test_products_count(driver):
    """Verify products page has products."""
    driver.get("http://localhost:5000/products")
    products = WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(By.CLASS_NAME, "product-card")
    )
    assert len(products) _____ 0                         # 8. Comparison operator


def test_will_fail(driver):
    """This test SHOULD fail — to demonstrate screenshot on failure."""
    driver.get("http://localhost:5000")
    driver.find_element(By.ID, "this-element-does-not-exist")


# ── Run all tests ────────────────────────────────────────────────────────────
driver = webdriver.Chrome()
driver.maximize_window()

results = []
for name, func in [
    ("test_home_page", test_home_page),
    ("test_login_valid", test_login_valid),
    ("test_products_count", test_products_count),
    ("test_will_fail", test_will_fail),
]:
    results.append(run_test(driver, name, func))

driver._____()                                           # 9. Close all windows

# Summary
passed = sum(results)
total = len(results)
print(f"\n{'='*40}")
print(f"Results: {passed}/{total} tests passed")
