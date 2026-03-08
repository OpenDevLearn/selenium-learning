"""
Day 03 - Homework Exercise 4: iFrame Interactions
===================================================
TASK: Navigate to /frames and:

  1. Switch to the "main-frame" iframe
     - Get the title text inside it
     - Click the button inside the frame
     - Verify the result text
     - Type "Hello World" into the input inside the frame

  2. Switch back to the main page

  3. Switch to the "outer-frame" iframe
     - Read the outer frame title
     - Switch into the nested "inner-frame"
     - Click the button inside the inner frame
     - Type "Nested Frame Text" into the input

  4. Go back to the parent frame
  5. Go back to the main page

Print what you find at each step.

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# YOUR CODE HERE
