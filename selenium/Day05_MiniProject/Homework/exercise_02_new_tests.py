"""
Day 05 - Homework Exercise 2: Write 5 New Test Cases
======================================================
TASK: Using the Page Object Model from the session, write 5 NEW test cases
that were NOT covered in the session's test_suite.py.

Ideas for new tests:
  1. Test that the home page has all 6 feature cards
  2. Test that adding multiple products to the cart shows correct count
  3. Test the product search with a term that returns zero results
  4. Test navigation links in the navbar all work
  5. Test that the form page has all expected input types
  6. Test that logging out clears the session (can't access dashboard)
  7. Test that the cart updates correctly when removing items

Pick 5 and implement them using the POM pattern.

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

# YOUR CODE HERE
