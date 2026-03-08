"""
Day 04 - Session Program 2: Explicit Wait with Expected Conditions
====================================================================
The recommended approach for production-quality tests.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/dynamic")

# ── 1. Wait for element to be present ───────────────────────────────────────
print("=== 1. presence_of_element_located ===")
# Element already exists in DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dynamic-title"))
)
print(f"Element found: {element.text}")

# ── 2. Wait for dynamically loaded content ──────────────────────────────────
print("\n=== 2. Waiting for AJAX content ===")
driver.find_element(By.ID, "load-content-btn").click()
print("Clicked 'Load Content' — waiting for data (2s server delay)...")

# Wait for the dynamic content div to become visible
content = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.ID, "dynamic-content"))
)
print(f"Content loaded! Text: {content.text[:80]}...")

# ── 3. Wait for element to be clickable ──────────────────────────────────────
print("\n=== 3. element_to_be_clickable ===")
btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "start-countdown-btn"))
)
print(f"Button is clickable: {btn.text}")

# ── 4. Wait for text to appear in element ────────────────────────────────────
print("\n=== 4. Countdown with text wait ===")
driver.find_element(By.ID, "start-countdown-btn").click()

# Wait for "Countdown Complete!" to appear
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "countdown-complete"))
)
complete = driver.find_element(By.ID, "countdown-complete")
print(f"Countdown finished: {complete.text}")

# ── 5. Wait for element to disappear ────────────────────────────────────────
print("\n=== 5. invisibility_of_element_located ===")
# Toggle element to hide it
driver.find_element(By.ID, "toggle-element-btn").click()

WebDriverWait(driver, 5).until(
    EC.invisibility_of_element_located((By.ID, "togglable-element"))
)
print("Togglable element is now hidden!")

# Toggle it back
driver.find_element(By.ID, "toggle-element-btn").click()
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "togglable-element"))
)
print("Togglable element is visible again!")

# ── 6. Wait for URL change ──────────────────────────────────────────────────
print("\n=== 6. url_contains ===")
driver.get("http://localhost:5000/login")
driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "login-btn").click()

WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
print(f"URL changed to: {driver.current_url}")

# ── 7. Wait for title ───────────────────────────────────────────────────────
print("\n=== 7. title_contains ===")
driver.get("http://localhost:5000")
WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
print(f"Title: {driver.title}")

driver.quit()
print("\nExplicit wait examples done!")
