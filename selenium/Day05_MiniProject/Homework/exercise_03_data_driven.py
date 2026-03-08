"""
Day 05 - Homework Exercise 3: Data-Driven Testing
===================================================
TASK: Write data-driven tests that run the SAME test logic with DIFFERENT data.

  1. Data-driven login test:
     Run the login test with these data sets:
       - ("testuser", "password123", True)    → should succeed
       - ("wronguser", "wrongpass", False)     → should fail
       - ("testuser", "wrongpass", False)      → should fail
       - ("", "password123", False)            → empty username
       - ("testuser", "", False)               → empty password

  2. Data-driven product search:
     Search for these terms and verify the expected count:
       - ("Laptop", 1)
       - ("Book", 2)        → Python Book + Selenium Guide
       - ("xyz_nothing", 0) → no results
       - ("USB", 1)

For each test, print the input data and the PASS/FAIL result.

HINT: Store test data in a list of tuples, then loop through them.

Write your code below:
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Session'))

from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# YOUR CODE HERE
