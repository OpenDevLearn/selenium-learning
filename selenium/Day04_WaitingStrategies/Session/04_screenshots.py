"""
Day 04 - Session Program 4: Screenshots
=========================================
Taking screenshots of pages and specific elements.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Create screenshots directory
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()

# ── 1. Full page screenshot ─────────────────────────────────────────────────
print("=== 1. Full Page Screenshot ===")
driver.get("http://localhost:5000")
time.sleep(1)

filepath = os.path.join(SCREENSHOT_DIR, "homepage.png")
driver.save_screenshot(filepath)
print(f"Saved: {filepath}")

# ── 2. Element screenshot ───────────────────────────────────────────────────
print("\n=== 2. Element Screenshot ===")
driver.get("http://localhost:5000/products")
time.sleep(1)

first_card = driver.find_element(By.CSS_SELECTOR, ".product-card")
filepath = os.path.join(SCREENSHOT_DIR, "first_product.png")
first_card.screenshot(filepath)
print(f"Saved: {filepath}")

# ── 3. Screenshot on failure pattern ────────────────────────────────────────
print("\n=== 3. Screenshot on Failure ===")

def safe_find(driver, by, value, screenshot_name="error"):
    """Find an element, take screenshot if it fails."""
    try:
        return driver.find_element(by, value)
    except Exception as e:
        filepath = os.path.join(SCREENSHOT_DIR, f"{screenshot_name}.png")
        driver.save_screenshot(filepath)
        print(f"❌ Element not found! Screenshot saved: {filepath}")
        raise

# This will work:
element = safe_find(driver, By.ID, "products-title", "products_title")
print(f"Found: {element.text}")

# This will fail and take a screenshot:
try:
    safe_find(driver, By.ID, "nonexistent", "failure_example")
except Exception:
    print("Failure screenshot taken (as expected)")

# ── 4. Multiple screenshots during a flow ────────────────────────────────────
print("\n=== 4. Flow Screenshots ===")

driver.get("http://localhost:5000/login")
time.sleep(1)
driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "step1_login_page.png"))

driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "step2_filled_form.png"))

driver.find_element(By.ID, "login-btn").click()
WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
driver.save_screenshot(os.path.join(SCREENSHOT_DIR, "step3_dashboard.png"))

print("Flow screenshots saved: step1, step2, step3")

driver.quit()
print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")
