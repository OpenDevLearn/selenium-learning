"""
Day 01 - Session Program 2: Browser Navigation
================================================
Learn navigation commands: back, forward, refresh, and visiting multiple pages.
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the home page
driver.get("http://localhost:5000")
print(f"1. Home Page → Title: {driver.title}")
print(f"   URL: {driver.current_url}")

# Navigate to the Products page
driver.get("http://localhost:5000/products")
print(f"\n2. Products Page → Title: {driver.title}")
print(f"   URL: {driver.current_url}")

# Navigate to the Login page
driver.get("http://localhost:5000/login")
print(f"\n3. Login Page → Title: {driver.title}")
print(f"   URL: {driver.current_url}")

# Go back to Products page
driver.back()
print(f"\n4. After back() → URL: {driver.current_url}")

# Go forward to Login page again
driver.forward()
print(f"5. After forward() → URL: {driver.current_url}")

# Refresh the current page
driver.refresh()
print(f"6. After refresh() → URL: {driver.current_url}")

# Clean up
driver.quit()
print("\nDone! Browser closed.")
