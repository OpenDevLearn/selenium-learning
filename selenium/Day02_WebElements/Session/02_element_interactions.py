"""
Day 02 - Session Program 2: Element Interactions
==================================================
Learn to interact with web elements: click, type, clear, submit.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/login")
time.sleep(1)

# ── Type into input fields ──────────────────────────────────────────────────
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# send_keys() types text into the input
username_field.send_keys("testuser")
print(f"Typed username: '{username_field.get_attribute('value')}'")

password_field.send_keys("password123")
print(f"Typed password: (hidden)")

# ── Check element states ────────────────────────────────────────────────────
print(f"\nUsername displayed? {username_field.is_displayed()}")
print(f"Username enabled?  {username_field.is_enabled()}")

# Check the "Remember me" checkbox
remember = driver.find_element(By.ID, "remember-me")
print(f"Remember me selected? {remember.is_selected()}")

remember.click()
print(f"After click, selected? {remember.is_selected()}")

# ── Click the login button ──────────────────────────────────────────────────
login_btn = driver.find_element(By.ID, "login-btn")
print(f"\nButton text: '{login_btn.text}'")
print(f"Button enabled? {login_btn.is_enabled()}")

login_btn.click()
time.sleep(1)

# ── Verify login success ────────────────────────────────────────────────────
print(f"\nAfter login:")
print(f"Current URL: {driver.current_url}")
print(f"Page title:  {driver.title}")

# Check for the dashboard heading
try:
    heading = driver.find_element(By.ID, "dashboard-title")
    print(f"Dashboard heading: '{heading.text}'")
    print("✅ Login successful!")
except Exception:
    print("❌ Login failed!")

driver.quit()
