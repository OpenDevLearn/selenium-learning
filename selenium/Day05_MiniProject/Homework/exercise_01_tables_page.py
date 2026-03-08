"""
Day 05 - Homework Exercise 1: Create a Tables Page Object
===========================================================
TASK: Create a page object for the Tables page (/tables) following the POM pattern.

Your TablesPage class should have:
  - Locators for: table, headers, rows, search box, modal elements
  - Methods for:
    - open() — navigate to /tables
    - get_headers() — return list of header texts
    - get_row_count() — return number of employee rows
    - get_employee_data() — return list of dicts with employee info
    - search(query) — type in the search box and filter
    - get_visible_row_count() — return count of visible rows after filtering
    - view_employee(index) — click the View button for a specific row
    - get_modal_name() — get the name shown in the modal
    - close_modal() — close the modal

After creating the page object, write 3 test functions that use it:
  1. Verify all employees are loaded (10 rows)
  2. Search for "Engineering" and verify the count
  3. Click View on an employee and verify the modal content

Write your code below:
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Session'))

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# YOUR CODE HERE — Create the TablesPage class and test functions
