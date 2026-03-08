"""
Day 03 - Session Program 5: Working with Tables
=================================================
Read, validate, and manipulate table data.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/tables")
time.sleep(1)

# ── 1. Get all table headers ────────────────────────────────────────────────
headers = driver.find_elements(By.CSS_SELECTOR, "#employee-table thead th")
header_texts = [h.text for h in headers]
print(f"Headers: {header_texts}")

# ── 2. Count rows ───────────────────────────────────────────────────────────
rows = driver.find_elements(By.CSS_SELECTOR, "#employee-tbody tr")
print(f"Total rows: {len(rows)}")

# ── 3. Read all data row by row ─────────────────────────────────────────────
print("\n=== All Employee Data ===")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    emp_id = cells[0].text
    name = cells[1].text
    dept = cells[2].text
    salary = cells[3].text
    email = cells[4].text
    print(f"  {emp_id}. {name} | {dept} | {salary} | {email}")

# ── 4. Get specific cell (row 3, column 2 = Name) ───────────────────────────
cell = driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]")
print(f"\nRow 3, Col 2 (Name): {cell.text}")

# ── 5. Extract all salaries and find max ─────────────────────────────────────
salary_cells = driver.find_elements(By.CSS_SELECTOR, ".emp-salary")
salaries = []
for cell in salary_cells:
    value = float(cell.text.replace("$", "").replace(",", ""))
    salaries.append(value)

print(f"\nSalaries: {salaries}")
print(f"Max salary: ${max(salaries):,.2f}")
print(f"Min salary: ${min(salaries):,.2f}")
print(f"Avg salary: ${sum(salaries)/len(salaries):,.2f}")

# ── 6. Filter by department ─────────────────────────────────────────────────
dept_cells = driver.find_elements(By.CSS_SELECTOR, ".emp-dept")
dept_name_pairs = []
for row in rows:
    name = row.find_element(By.CLASS_NAME, "emp-name").text
    dept = row.find_element(By.CLASS_NAME, "emp-dept").text
    dept_name_pairs.append((dept, name))

print("\n=== Engineering Department ===")
for dept, name in dept_name_pairs:
    if dept == "Engineering":
        print(f"  {name}")

# ── 7. Click a button in a specific row ──────────────────────────────────────
print("\n=== Clicking View on first employee ===")
first_view_btn = rows[0].find_element(By.CLASS_NAME, "view-btn")
first_view_btn.click()
time.sleep(1)

# Read modals content
modal_name = driver.find_element(By.ID, "modal-name").text
modal_email = driver.find_element(By.ID, "modal-email").text
print(f"Modal - Name: {modal_name}, Email: {modal_email}")

# Close modal
driver.find_element(By.ID, "modal-close").click()
time.sleep(0.5)

# ── 8. Table search ─────────────────────────────────────────────────────────
print("\n=== Table Search ===")
search_box = driver.find_element(By.ID, "table-search")
search_box.send_keys("Engineering")
time.sleep(0.5)

visible_rows = [r for r in driver.find_elements(By.CSS_SELECTOR, "#employee-tbody tr")
                if r.is_displayed()]
print(f"Visible rows after search 'Engineering': {len(visible_rows)}")

driver.quit()
print("\nTable examples done!")
