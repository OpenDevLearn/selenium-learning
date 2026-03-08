# Day 03 — Actions, Assertions & Advanced Interactions

## Topics Covered

### 1. Dropdown & Select Elements
- `Select` class from `selenium.webdriver.support.ui`
- `select_by_visible_text()`, `select_by_value()`, `select_by_index()`
- Getting selected option, all options

### 2. Working with Checkboxes & Radio Buttons
- Clicking / toggling checkboxes
- Selecting radio buttons
- Verifying selection state with `is_selected()`

### 3. Form Automation (Complex Forms)
- Filling out the complete practice form
- Handling all input types: text, email, date, radio, checkbox, select, textarea, range, color

### 4. JavaScript Alerts, Confirms, and Prompts
- `driver.switch_to.alert`
- `.accept()`, `.dismiss()`, `.text`, `.send_keys()`

### 5. ActionChains — Advanced User Interactions
- `ActionChains(driver)` for complex interactions
- Hover (`.move_to_element()`)
- Double click (`.double_click()`)
- Right click (`.context_click()`)
- Drag and drop (`.drag_and_drop()`)
- Keyboard actions (`.key_down()`, `.key_up()`, `.send_keys()`)

### 6. Handling Tables
- Reading table data row by row
- Extracting specific cells
- Sorting verification

### 7. Working with Multiple Windows/Tabs
- `driver.window_handles`
- `driver.switch_to.window(handle)`

### 8. Working with iFrames
- `driver.switch_to.frame()`
- `driver.switch_to.default_content()`
- Nested frames

---

## Homework

See the `Homework/` folder:

1. **Exercise 1:** Fill out the complete practice form and verify the result.
2. **Exercise 2:** Handle all three types of JavaScript alerts.
3. **Exercise 3:** Complete partial code for table data extraction.
4. **Exercise 4:** Work with iFrames (interact with elements inside frames).
5. **Exercise 5 (Challenge):** Full shopping cart workflow — browse, add items, verify cart, checkout.
