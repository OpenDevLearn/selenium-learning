"""
Day 02 - Homework Exercise 5 (Challenge): Full Registration Flow
==================================================================
TASK: Automate the full registration + login flow:
  1. Navigate to /register
  2. Fill in all fields with a UNIQUE username (e.g., "student_" + some number)
  3. Submit the registration form
  4. Verify the success message appears
  5. Navigate to /login
  6. Login with the credentials you just registered
  7. Verify you reach the dashboard
  8. Read and print the profile information from the dashboard
  9. Logout
  10. Try to register the SAME username again and verify the error message

HINT: Use str(time.time()) to generate a unique suffix for the username.

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# YOUR CODE HERE
