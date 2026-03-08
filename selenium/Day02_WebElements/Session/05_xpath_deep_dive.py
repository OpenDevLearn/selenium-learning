"""
Day 02 - Session Program 5: XPath Deep Dive
=============================================
Master XPath expressions for powerful element location.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/login")
time.sleep(1)

print("=== XPath Examples ===\n")

# ── Basic attribute match ───────────────────────────────────────────────────
el = driver.find_element(By.XPATH, "//input[@id='username']")
print(f"//input[@id='username']        → placeholder: {el.get_attribute('placeholder')}")

# ── By text content ─────────────────────────────────────────────────────────
el = driver.find_element(By.XPATH, "//h2[text()='Login']")
print(f"//h2[text()='Login']           → tag: <{el.tag_name}>")

# ── contains() function ─────────────────────────────────────────────────────
el = driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]")
print(f"contains(text(), 'Register')   → '{el.text}'")

el = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'username')]")
print(f"contains(@placeholder, 'user') → id: {el.get_attribute('id')}")

# ── starts-with() ───────────────────────────────────────────────────────────
els = driver.find_elements(By.XPATH, "//a[starts-with(@id, 'nav')]")
print(f"starts-with(@id, 'nav')        → {len(els)} elements")

# ── Multiple conditions with and/or ─────────────────────────────────────────
el = driver.find_element(By.XPATH, "//input[@type='text' and @id='username']")
print(f"[@type='text' and @id='...']   → name: {el.get_attribute('name')}")

# ── Parent axis ─────────────────────────────────────────────────────────────
el = driver.find_element(By.XPATH, "//input[@id='username']/parent::div")
print(f"parent::div of username        → class: {el.get_attribute('class')}")

# ── Following-sibling axis ──────────────────────────────────────────────────
# Navigate to tables for more structured examples
driver.get("http://localhost:5000/tables")
time.sleep(1)

print(f"\n--- Tables Page XPath ---")

# Find all rows
rows = driver.find_elements(By.XPATH, "//tbody[@id='employee-tbody']/tr")
print(f"//tbody/tr                     → {len(rows)} employee rows")

# Get specific cell from specific row
cell = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]")
print(f"//tbody/tr[1]/td[2]            → First employee: {cell.text}")

# Find row by cell content
row = driver.find_element(By.XPATH, "//td[text()='Engineering']/parent::tr/td[2]")
print(f"Row with 'Engineering'         → Name: {row.text}")

# Get all employees in Engineering
eng_names = driver.find_elements(
    By.XPATH, "//td[text()='Engineering']/preceding-sibling::td[@class='emp-name']"
)
print(f"Engineering employees          → {[n.text for n in eng_names]}")

# Last row
last = driver.find_element(By.XPATH, "//tbody/tr[last()]/td[@class='emp-name']")
print(f"//tbody/tr[last()]/td          → Last employee: {last.text}")

# Position-based
third = driver.find_element(By.XPATH, "//tbody/tr[position()=3]/td[@class='emp-name']")
print(f"//tbody/tr[position()=3]       → Third employee: {third.text}")

driver.quit()
print("\nXPath examples done!")
