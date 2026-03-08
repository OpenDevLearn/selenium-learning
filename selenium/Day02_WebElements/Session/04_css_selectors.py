"""
Day 02 - Session Program 4: CSS Selectors Deep Dive
=====================================================
Master CSS selectors for precise element location.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000")
time.sleep(1)

print("=== CSS Selector Examples ===\n")

# ── By ID (#) ───────────────────────────────────────────────────────────────
el = driver.find_element(By.CSS_SELECTOR, "#page-title")
print(f"#page-title         → '{el.text}'")

# ── By Class (.) ────────────────────────────────────────────────────────────
el = driver.find_element(By.CSS_SELECTOR, ".navbar-brand")
print(f".navbar-brand       → '{el.text}'")

# ── By Tag ──────────────────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, "h5")
print(f"h5                  → Found {len(els)} <h5> elements")

# ── Tag + Class ─────────────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, "a.nav-link")
print(f"a.nav-link          → Found {len(els)} nav links")

# ── Attribute selector ──────────────────────────────────────────────────────
el = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
print(f"a[href='/products'] → '{el.text}'")

# ── Attribute starts with (^=) ──────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, "a[href^='/']")
print(f"a[href^='/']        → {len(els)} links starting with /")

# ── Attribute contains (*=) ─────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, "a[id*='nav']")
print(f"a[id*='nav']        → {len(els)} elements with 'nav' in id")

# ── Direct child (>) ────────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, ".navbar-nav > li")
print(f".navbar-nav > li    → {len(els)} direct child <li> elements")

# ── Descendant (space) ──────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, "#navbarNav a")
print(f"#navbarNav a        → {len(els)} links inside navbarNav")

# ── nth-child ───────────────────────────────────────────────────────────────
el = driver.find_element(By.CSS_SELECTOR, ".card:first-child")
print(f".card:first-child   → First card found")

# Navigate to products for more examples
driver.get("http://localhost:5000/products")
time.sleep(1)

# ── Combining selectors ────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, ".product-card .card-title")
print(f"\n--- Products Page ---")
print(f".product-card .card-title → {len(els)} product titles")

# ── Multiple classes ────────────────────────────────────────────────────────
els = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-primary")
print(f".btn.btn-primary          → {len(els)} primary buttons")

driver.quit()
print("\nCSS Selector examples done!")
