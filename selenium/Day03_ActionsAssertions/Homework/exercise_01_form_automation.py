"""
Day 03 - Homework Exercise 1: Complete Form Automation
=======================================================
TASK: Fill out the entire practice form at /practice-forms with these values:
  - First Name: "Test"
  - Last Name: "Student"
  - Email: "student@test.com"
  - Date of Birth: any date
  - Gender: Female
  - Hobbies: Check "Music" and "Travel"
  - Country: "UK"
  - Experience: 7 (using range slider)
  - Message: "Automated by Selenium"
  - Agree to terms: Yes

After submitting, verify ALL fields on the result page match what you entered.
Print PASS or FAIL for each field.

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# YOUR CODE HERE
