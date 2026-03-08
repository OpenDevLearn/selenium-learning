"""
Day 02 - Session Program 6: Working with Forms (Login Automation)
==================================================================
Automate a login flow and verify the result.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ── Test 1: Successful Login ────────────────────────────────────────────────
print("=== Test 1: Valid Login ===")
driver.get("http://localhost:5000/login")
time.sleep(1)

driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login-btn").click()
time.sleep(1)

if "dashboard" in driver.current_url.lower():
    welcome = driver.find_element(By.ID, "dashboard-title")
    print(f"  ✅ Login successful! → {welcome.text}")
else:
    print("  ❌ Login failed!")

# Logout
driver.get("http://localhost:5000/logout")
time.sleep(1)

# ── Test 2: Failed Login ────────────────────────────────────────────────────
print("\n=== Test 2: Invalid Login ===")
driver.get("http://localhost:5000/login")
time.sleep(1)

driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "login-btn").click()
time.sleep(1)

try:
    error = driver.find_element(By.ID, "login-error")
    print(f"  ✅ Error shown: '{error.text}'")
except Exception:
    print("  ❌ Error message not found!")

# ── Test 3: Clear and retype ────────────────────────────────────────────────
print("\n=== Test 3: Clear and Retype ===")
username_field = driver.find_element(By.ID, "username")
print(f"  Current value: '{username_field.get_attribute('value')}'")

username_field.clear()
print(f"  After clear:   '{username_field.get_attribute('value')}'")

username_field.send_keys("testuser")
print(f"  After retype:  '{username_field.get_attribute('value')}'")

driver.quit()
print("\nForm automation done!")
