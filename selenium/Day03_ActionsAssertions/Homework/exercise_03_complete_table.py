"""
Day 03 - Homework Exercise 3: Complete the Table Extractor
============================================================
TASK: Fill in the blanks (marked with _____) to extract employee data.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/tables")
time.sleep(1)

# Get all rows from the table body
rows = driver.find_elements(By.CSS_SELECTOR, _____)     # 1. CSS for rows in employee-tbody

employees = []
for row in rows:
    cells = row.find_elements(_____, _____)              # 2. Find all <td> in each row
    employee = {
        "id": cells[0]._____,                            # 3. Get the text of the cell
        "name": cells[1].text,
        "department": cells[_____].text,                  # 4. Index for department column
        "salary": cells[3].text,
        "email": cells[_____].text,                       # 5. Index for email column
    }
    employees.append(employee)

# Print all employees
print("All Employees:")
for emp in employees:
    print(f"  {emp['id']}. {emp['name']} ({emp['department']}) - {emp['salary']}")

# Find all employees in the 'Engineering' department
engineering = [e for e in employees if e[_____] == "Engineering"]    # 6. Key name
print(f"\nEngineering employees ({len(engineering)}):")
for emp in engineering:
    print(f"  - {emp['name']}")

# Find the highest paid employee
salaries = [(e['name'], float(e['salary'].replace('$', '').replace(',', '')))
            for e in employees]
highest = _____(salaries, key=lambda x: x[1])            # 7. Function to find maximum
print(f"\nHighest paid: {highest[0]} (${highest[1]:,.2f})")

# Count employees per department
departments = {}
for emp in employees:
    dept = emp['department']
    departments[dept] = departments._____(dept, 0) + 1    # 8. dict method for default value
print(f"\nEmployees per department: {departments}")

driver._____()                                            # 9. Close all windows
