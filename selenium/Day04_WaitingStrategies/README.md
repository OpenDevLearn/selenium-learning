# Day 04 — Waiting Strategies, Screenshots & File Handling

## Topics Covered

### 1. Why Waits Matter
- Race conditions between script and browser
- Common `NoSuchElementException` caused by timing issues
- Why `time.sleep()` is bad practice (but useful for learning)

### 2. Implicit Waits
- `driver.implicitly_wait(seconds)`
- Global setting — applies to ALL `find_element` calls
- Pros and cons

### 3. Explicit Waits (WebDriverWait + Expected Conditions)
- `WebDriverWait(driver, timeout).until(condition)`
- Common Expected Conditions:
  - `presence_of_element_located`
  - `visibility_of_element_located`
  - `element_to_be_clickable`
  - `text_to_be_present_in_element`
  - `invisibility_of_element_located`
  - `alert_is_present`
  - `title_contains`
  - `url_contains`

### 4. Fluent Waits
- Custom polling frequency
- Ignoring specific exceptions

### 5. Page Load Timeout
- `driver.set_page_load_timeout(seconds)`

### 6. Screenshots
- `driver.save_screenshot("filename.png")`
- `element.screenshot("element.png")`
- Taking screenshots on failure

### 7. File Upload
- `send_keys()` with file path on `<input type="file">`

### 8. Executing JavaScript
- `driver.execute_script("javascript code")`
- Scrolling, hidden elements, getting computed styles

---

## Homework

See the `Homework/` folder:

1. **Exercise 1:** Use explicit waits with the dynamic content page.
2. **Exercise 2:** Handle the countdown timer with proper waits.
3. **Exercise 3:** Complete the code for screenshot-on-failure pattern.
4. **Exercise 4:** File upload automation.
5. **Exercise 5 (Challenge):** Build a robust test for the slow-loading page + AJAX content.
