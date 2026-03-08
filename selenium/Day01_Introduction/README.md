# Day 01 — Introduction to Selenium WebDriver

## Topics Covered

### 1. What is Selenium?
- Overview of Selenium suite (IDE, WebDriver, Grid)
- Why Selenium WebDriver is the industry standard for browser automation
- Use cases: functional testing, regression testing, web scraping

### 2. Environment Setup
- Installing Python 3.12 (Conda environment)
- Installing Selenium: `pip install selenium`
- Installing ChromeDriver (or using `webdriver-manager`)
- Verifying the setup

### 3. First Selenium Script
- Launching Chrome browser
- Navigating to a URL
- Getting page title and current URL
- Closing vs quitting the browser

### 4. WebDriver Basics
- `webdriver.Chrome()` — launching a browser
- `driver.get(url)` — navigating to a page
- `driver.title` — getting the page title
- `driver.current_url` — getting the current URL
- `driver.page_source` — getting the page HTML
- `driver.close()` vs `driver.quit()`
- `driver.maximize_window()` / `driver.minimize_window()`
- `driver.back()` / `driver.forward()` / `driver.refresh()`

### 5. Browser Options
- Headless mode
- Disabling notifications
- Setting window size

### 6. Introduction to the Practice Application
- Starting the Docker Compose setup
- Exploring the practice app pages

---

## Demo Credentials (Practice App)
- **URL:** http://localhost:5000
- **Username:** `testuser`
- **Password:** `password123`

---

## Homework

See the `Homework/` folder for exercises:

1. **Exercise 1:** Write a script to open the practice app, print the title, and close the browser.
2. **Exercise 2:** Navigate to multiple pages and print the URLs.
3. **Exercise 3:** Use headless mode to get the page source and count occurrences of a word.
4. **Exercise 4 (Challenge):** Complete the partial code snippet provided.
5. **Exercise 5 (Creative):** Write a script that navigates through all nav links and prints each page title.
