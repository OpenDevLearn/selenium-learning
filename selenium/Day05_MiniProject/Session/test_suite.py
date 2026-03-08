"""
Day 05 - Session: Complete Test Suite using Page Object Model
==============================================================
A real-world test suite demonstrating how QA engineers write tests.

Usage:
  cd Day05_MiniProject/Session
  python test_suite.py
"""

import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Add the current directory to path so we can import pages
sys.path.insert(0, os.path.dirname(__file__))

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.dashboard_page import DashboardPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.base_page import SCREENSHOT_DIR


# ── Test Runner ──────────────────────────────────────────────────────────────

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.results = []

    def record(self, name, passed, message=""):
        status = "PASS" if passed else "FAIL"
        self.results.append((name, status, message))
        if passed:
            self.passed += 1
        else:
            self.failed += 1
        print(f"  {'✅' if passed else '❌'} {name}" + (f" — {message}" if message else ""))


def run_test(driver, test_func, result):
    """Run a single test with error handling and screenshot on failure."""
    test_name = test_func.__name__
    print(f"\n▶ Running: {test_name}")
    try:
        test_func(driver, result)
    except Exception as e:
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"{test_name}_ERROR.png")
        driver.save_screenshot(screenshot_path)
        result.record(test_name, False, f"Unhandled error: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

def test_01_login_valid(driver, result):
    """Test: Login with valid credentials."""
    page = LoginPage(driver)
    page.open()
    page.login("testuser", "password123")

    dashboard = DashboardPage(driver)
    dashboard.wait_for_url("dashboard")

    welcome = dashboard.get_welcome_text()
    result.record("Login redirects to dashboard", "dashboard" in driver.current_url)
    result.record("Dashboard shows welcome text", "Welcome" in welcome, welcome)

    dashboard.logout()


def test_02_login_invalid(driver, result):
    """Test: Login with invalid credentials shows error."""
    page = LoginPage(driver)
    page.open()
    time.sleep(0.5)

    # Type credentials
    from selenium.webdriver.common.by import By
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys("wrongpass")

    # Submit via form submit instead of button click
    driver.find_element(By.ID, "login-form").submit()
    time.sleep(1)

    has_error = page.is_error_displayed()
    result.record("Invalid login shows error", has_error)

    if has_error:
        error_text = page.get_error_message()
        result.record("Error message is correct", "Invalid" in error_text, error_text)

    if has_error:
        error_text = page.get_error_message()
        result.record("Error message is correct", "Invalid" in error_text, error_text)


def test_03_register_new_user(driver, result):
    """Test: Register a new user."""
    page = RegisterPage(driver)
    page.open()

    # Create unique username
    unique_id = str(int(time.time()))[-6:]
    username = f"student_{unique_id}"
    email = f"student_{unique_id}@test.com"

    page.register(
        full_name="Test Student",
        username=username,
        email=email,
        password="securepass123"
    )

    success = page.is_success_displayed()
    result.record("Registration shows success", success)

    if success:
        msg = page.get_success_message()
        result.record("Success message mentions login", "login" in msg.lower(), msg)

    # Verify can login with new credentials
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, "securepass123")

    dashboard = DashboardPage(driver)
    dashboard.wait_for_url("dashboard")
    result.record("New user can login", "dashboard" in driver.current_url)
    dashboard.logout()


def test_04_register_duplicate_user(driver, result):
    """Test: Registering with existing username shows error."""
    page = RegisterPage(driver)
    page.open()
    page.register(
        full_name="Duplicate User",
        username="testuser",
        email="unique@test.com",
        password="password123"
    )

    error = page.get_error_message()
    result.record("Duplicate username shows error", "already exists" in error.lower(), error)


def test_05_register_password_mismatch(driver, result):
    """Test: Mismatched passwords show error."""
    page = RegisterPage(driver)
    page.open()

    unique_id = str(int(time.time()))[-6:]
    page.register(
        full_name="Mismatch User",
        username=f"mismatch_{unique_id}",
        email=f"mismatch_{unique_id}@test.com",
        password="password1",
        confirm_password="password2"
    )

    error = page.get_error_message()
    result.record("Password mismatch shows error", "do not match" in error.lower(), error)


def test_06_products_listing(driver, result):
    """Test: Products page shows products."""
    page = ProductsPage(driver)
    page.open()

    count = page.get_total_products()
    result.record("Products are displayed", count > 0, f"{count} products found")

    names = page.get_product_names()
    result.record("Product names are not empty", all(n.strip() for n in names))

    prices = page.get_product_prices()
    result.record("Products have prices", all("$" in p for p in prices))


def test_07_product_search(driver, result):
    """Test: Product search filters results."""
    page = ProductsPage(driver)
    page.open()

    total_before = page.get_total_products()
    page.search_product("Laptop")

    names = page.get_product_names()
    result.record("Search returns results", len(names) > 0, f"{len(names)} results")
    result.record("Search results match query", any("Laptop" in n for n in names))
    result.record("Search filters results", len(names) <= total_before)


def test_08_product_category_filter(driver, result):
    """Test: Category filter works."""
    page = ProductsPage(driver)
    page.open()

    total_before = page.get_total_products()
    page.filter_by_category("Electronics")

    total_after = page.get_total_products()
    result.record("Category filter reduces results", total_after <= total_before)
    result.record("Filtered products exist", total_after > 0, f"{total_after} Electronics products")


def test_09_shopping_cart_workflow(driver, result):
    """Test: Full shopping cart workflow."""
    # Add items to cart
    products = ProductsPage(driver)
    products.open()

    product_names = products.get_product_names()
    first_product = product_names[0] if product_names else "Unknown"

    products.add_product_to_cart(0)

    # Check cart
    cart = CartPage(driver)
    cart.open()

    item_count = cart.get_item_count()
    result.record("Cart has 1 item", item_count == 1, f"Found {item_count}")

    cart_items = cart.get_item_names()
    result.record("Cart shows correct product", first_product in cart_items,
                  f"Expected '{first_product}' in {cart_items}")

    total = cart.get_grand_total()
    result.record("Cart shows total", "$" in total, total)

    # Checkout
    cart.checkout()
    result.record("Checkout redirects to products", "products" in driver.current_url.lower())

    # Verify cart is empty after checkout
    cart.open()
    result.record("Cart is empty after checkout", cart.is_empty())


def test_10_dashboard_profile(driver, result):
    """Test: Dashboard shows correct profile info."""
    # Login first
    login = LoginPage(driver)
    login.open()
    login.login("testuser", "password123")

    dashboard = DashboardPage(driver)
    dashboard.wait_for_url("dashboard")

    profile = dashboard.get_profile_info()
    result.record("Profile shows username", profile["username"] == "testuser",
                  f"username: {profile['username']}")
    result.record("Profile shows email", "@" in profile["email"],
                  f"email: {profile['email']}")

    dashboard.logout()
    result.record("Logout redirects away from dashboard", "dashboard" not in driver.current_url)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN — Run all tests
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  SELENIUM PRACTICE APP — TEST SUITE")
    print("=" * 60)

    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    result = TestResult()

    tests = [
        test_01_login_valid,
        test_02_login_invalid,
        test_03_register_new_user,
        test_04_register_duplicate_user,
        test_05_register_password_mismatch,
        test_06_products_listing,
        test_07_product_search,
        test_08_product_category_filter,
        test_09_shopping_cart_workflow,
        test_10_dashboard_profile,
    ]

    for test_func in tests:
        run_test(driver, test_func, result)

    driver.quit()

    # ── Print Summary ────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  TEST RESULTS SUMMARY")
    print("=" * 60)

    for name, status, message in result.results:
        icon = "✅" if status == "PASS" else "❌"
        line = f"  {icon} {name}"
        if message:
            line += f" → {message}"
        print(line)

    print(f"\n  Total: {result.passed + result.failed}")
    print(f"  Passed: {result.passed}")
    print(f"  Failed: {result.failed}")
    rate = result.passed / (result.passed + result.failed) * 100 if (result.passed + result.failed) > 0 else 0
    print(f"  Pass Rate: {rate:.1f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
