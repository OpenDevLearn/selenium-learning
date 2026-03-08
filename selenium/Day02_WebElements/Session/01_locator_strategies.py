"""
Day 02 - Session Program 1: All 8 Locator Strategies
======================================================
Demonstrates every locator type available in Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/login")
time.sleep(1)

# ── 1. By.ID ───────────────────────────────────────────────────────────────
element = driver.find_element(By.ID, "username")
print(f"1. By.ID       → Tag: <{element.tag_name}>, Placeholder: {element.get_attribute('placeholder')}")

# ── 2. By.NAME ─────────────────────────────────────────────────────────────
element = driver.find_element(By.NAME, "password")
print(f"2. By.NAME     → Tag: <{element.tag_name}>, Type: {element.get_attribute('type')}")

# ── 3. By.CLASS_NAME ───────────────────────────────────────────────────────
element = driver.find_element(By.CLASS_NAME, "navbar-brand")
print(f"3. By.CLASS    → Text: {element.text}")

# ── 4. By.TAG_NAME ─────────────────────────────────────────────────────────
elements = driver.find_elements(By.TAG_NAME, "input")
print(f"4. By.TAG_NAME → Found {len(elements)} <input> elements")

# ── 5. By.LINK_TEXT ─────────────────────────────────────────────────────────
element = driver.find_element(By.LINK_TEXT, "Register here")
print(f"5. By.LINK_TEXT → Href: {element.get_attribute('href')}")

# ── 6. By.PARTIAL_LINK_TEXT ─────────────────────────────────────────────────
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Register")
print(f"6. By.PARTIAL  → Full text: '{element.text}'")

# ── 7. By.CSS_SELECTOR ─────────────────────────────────────────────────────
element = driver.find_element(By.CSS_SELECTOR, "#login-btn")
print(f"7. By.CSS      → Button text: '{element.text}'")

element2 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print(f"   By.CSS      → Input type: {element2.get_attribute('type')}")

# ── 8. By.XPATH ────────────────────────────────────────────────────────────
element = driver.find_element(By.XPATH, "//h2[@id='login-title']")
print(f"8. By.XPATH    → Heading: '{element.text}'")

element2 = driver.find_element(By.XPATH, "//button[text()='Login']")
print(f"   By.XPATH    → Button tag: <{element2.tag_name}>")

driver.quit()
print("\nAll 8 locator strategies demonstrated!")
