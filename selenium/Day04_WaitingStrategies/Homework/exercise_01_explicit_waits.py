"""
Day 04 - Homework Exercise 1: Explicit Waits with Dynamic Content
===================================================================
TASK: Navigate to /dynamic and:

  1. Click "Load Content (2s delay)"
  2. Use WebDriverWait (NOT time.sleep) to wait for the content to appear
  3. Once visible, extract and print:
     - The message text
     - All dynamically loaded list items
  4. Click "Load Notifications"
  5. Wait for at least 1 notification item to appear
  6. Print all notification texts

Do NOT use time.sleep() for any wait — only WebDriverWait with Expected Conditions!

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# YOUR CODE HERE
