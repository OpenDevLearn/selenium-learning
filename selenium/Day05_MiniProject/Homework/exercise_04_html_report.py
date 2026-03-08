"""
Day 05 - Homework Exercise 4 (Challenge): HTML Test Report
=============================================================
TASK: Create a test runner that generates an HTML test report.

  1. Run at least 10 test cases (mix of the ones you've written)
  2. For each test, record: name, status (PASS/FAIL), duration, error message
  3. Take a screenshot for each FAILED test
  4. Generate an HTML file "test_report.html" with:
     - Summary: total tests, passed, failed, pass rate
     - A table with all test results
     - Color coding: green for pass, red for fail
     - Timestamps
     - Links to failure screenshots (if any)

HINTS:
  - Use time.time() before and after each test to measure duration
  - Build the HTML as a string and write to file
  - You can use the test runner pattern from the session's test_suite.py

This is the final challenge — combine everything you've learned!

Write your code below:
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Session'))

from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.dashboard_page import DashboardPage
import time

# YOUR CODE HERE
