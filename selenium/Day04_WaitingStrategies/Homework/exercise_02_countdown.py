"""
Day 04 - Homework Exercise 2: Countdown Timer
===============================================
TASK: Navigate to /dynamic and:

  1. Click "Start 5s Countdown"
  2. Wait for the countdown to complete using WebDriverWait
     (wait for the "Countdown Complete!" element to become visible)
  3. Print the completion message
  4. Verify the countdown display is empty after completion
  5. BONUS: Start the countdown again and use a custom condition to
     wait until the countdown reaches "2" (not complete, just the number 2)

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# YOUR CODE HERE
