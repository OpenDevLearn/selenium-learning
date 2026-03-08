"""
Day 04 - Homework Exercise 4: File Upload
===========================================
TASK:
  1. Create a text file programmatically (use Python's open() function)
  2. Navigate to /file-upload
  3. Upload the file using send_keys on the file input
  4. Click the Upload button
  5. Wait for and verify the success message
  6. Clean up: delete the created text file

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tempfile

# YOUR CODE HERE
