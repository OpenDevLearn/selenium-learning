"""
Day 04 - Session Program 1: Implicit Wait
===========================================
Global wait applied to all find_element calls.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ── Set implicit wait (applies globally) ─────────────────────────────────────
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements

driver.get("http://localhost:5000/dynamic")

# This will work immediately — element exists right away
title = driver.find_element(By.ID, "dynamic-title")
print(f"Title found: {title.text}")

# ── Trying to find an element that doesn't exist ────────────────────────────
print("\nSearching for a non-existent element (will wait 10 seconds)...")
start_time = time.time()
try:
    driver.find_element(By.ID, "this-does-not-exist")
except Exception as e:
    elapsed = time.time() - start_time
    print(f"Element not found after {elapsed:.1f}s — NoSuchElementException")

# ── Implicit wait with dynamically added elements ────────────────────────────
print("\nClicking 'Add New Element'...")
driver.find_element(By.ID, "add-element-btn").click()

# Implicit wait will automatically wait up to 10s for this to appear
added = driver.find_element(By.ID, "added-element-1")
print(f"Found dynamically added element: '{added.text}'")

# ── Important: implicit wait is a GLOBAL setting ────────────────────────────
print(f"""
Key Points about Implicit Wait:
  ✅ Set ONCE, applies to ALL find_element calls
  ✅ Good for simple cases where elements just need time to load
  ❌ Cannot wait for specific conditions (visibility, clickability)
  ❌ Can slow down tests if elements truly don't exist (waits full timeout)
  ❌ Can cause unpredictable behavior when mixed with explicit waits
""")

driver.quit()
