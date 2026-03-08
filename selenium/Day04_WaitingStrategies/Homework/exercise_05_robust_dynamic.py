"""
Day 04 - Homework Exercise 5 (Challenge): Robust Dynamic Page Test
====================================================================
TASK: Build a comprehensive test suite for the dynamic content page.
Use ONLY explicit waits (WebDriverWait) — no time.sleep()!

  1. Navigate to /dynamic
  2. Click "Load Content" and wait for content to appear
     - Verify the message contains "loaded dynamically"
     - Count and print the dynamic items
  3. Start the countdown and wait for completion
     - Print "Countdown Complete" text
  4. Toggle the element twice:
     - First toggle: wait for it to disappear, verify
     - Second toggle: wait for it to reappear, verify
  5. Add 3 elements, use a custom condition to wait for all 3
  6. Navigate to /slow-page?delay=3
     - Set page load timeout appropriately
     - Verify the page loaded and shows the correct delay
  7. Take a screenshot after each major step

Report PASS/FAIL for each step.

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# YOUR CODE HERE
