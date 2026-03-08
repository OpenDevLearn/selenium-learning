"""
Day 03 - Session Program 1: Dropdowns & Select
=================================================
Working with <select> dropdowns using Selenium's Select class.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/practice-forms")
time.sleep(1)

# ── Find the Country dropdown ───────────────────────────────────────────────
dropdown_element = driver.find_element(By.ID, "country")
select = Select(dropdown_element)

# ── Method 1: Select by visible text ────────────────────────────────────────
select.select_by_visible_text("India")
time.sleep(0.5)
print(f"Selected by text:  {select.first_selected_option.text}")

# ── Method 2: Select by value attribute ──────────────────────────────────────
select.select_by_value("USA")
time.sleep(0.5)
print(f"Selected by value: {select.first_selected_option.text}")

# ── Method 3: Select by index (0-based) ─────────────────────────────────────
select.select_by_index(3)  # Canada (index 0 is the placeholder)
time.sleep(0.5)
print(f"Selected by index: {select.first_selected_option.text}")

# ── Get all available options ────────────────────────────────────────────────
print(f"\nAll options:")
for option in select.options:
    print(f"  - {option.text} (value='{option.get_attribute('value')}')")

# ── Count of options ─────────────────────────────────────────────────────────
print(f"\nTotal options: {len(select.options)}")

# ── Also works with the category filter on products page ─────────────────────
driver.get("http://localhost:5000/products")
time.sleep(1)

cat_dropdown = Select(driver.find_element(By.ID, "category-filter"))
print(f"\nProduct categories:")
for opt in cat_dropdown.options:
    print(f"  - {opt.text}")

driver.quit()
print("\nDropdown examples done!")
