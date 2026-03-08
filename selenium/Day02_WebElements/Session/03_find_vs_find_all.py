"""
Day 02 - Session Program 3: find_element vs find_elements
===========================================================
Understanding single vs multiple element queries.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/products")
time.sleep(1)

# ── find_element: returns the FIRST matching element ────────────────────────
first_product = driver.find_element(By.CLASS_NAME, "product-name")
print(f"First product: {first_product.text}")

# ── find_elements: returns a LIST of ALL matching elements ──────────────────
all_products = driver.find_elements(By.CLASS_NAME, "product-name")
print(f"\nTotal products found: {len(all_products)}")

print("\nAll product names:")
for i, product in enumerate(all_products, 1):
    print(f"  {i}. {product.text}")

# ── Getting prices ──────────────────────────────────────────────────────────
prices = driver.find_elements(By.CLASS_NAME, "product-price")
print("\nAll product prices:")
for price in prices:
    print(f"  {price.text}")

# ── Getting categories ──────────────────────────────────────────────────────
categories = driver.find_elements(By.CLASS_NAME, "product-category")
unique_cats = set(cat.text for cat in categories)
print(f"\nUnique categories: {unique_cats}")

# ── Handling element not found ──────────────────────────────────────────────
# find_element raises NoSuchElementException if not found
# find_elements returns an EMPTY LIST if none found
missing = driver.find_elements(By.CLASS_NAME, "nonexistent-class")
print(f"\nMissing elements (find_elements): {len(missing)} found (empty list, no error)")

try:
    driver.find_element(By.CLASS_NAME, "nonexistent-class")
except Exception as e:
    print(f"Missing element (find_element): Raises {type(e).__name__}")

driver.quit()
