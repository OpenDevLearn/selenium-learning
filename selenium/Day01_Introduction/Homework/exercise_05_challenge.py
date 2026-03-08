"""
Day 01 - Homework Exercise 5 (Challenge): Page Explorer
=========================================================
TASK: Write a script that:
  1. Opens the practice app home page
  2. Reads the page source to find all navigation links in the navbar
     (Hint: you can look for href patterns or just visit the known pages)
  3. Visits EACH of these pages: /, /products, /login, /register,
     /practice-forms, /tables, /dynamic, /interactions, /frames, /file-upload
  4. For each page, print:
       - The page title
       - The URL
       - The length of the page source (in characters)
  5. At the end, print a summary showing which page had the longest page source
  6. Close the browser

HINT: Use a list to store the page paths and loop through them.

Write your code below:
"""

from selenium import webdriver

# YOUR CODE HERE
