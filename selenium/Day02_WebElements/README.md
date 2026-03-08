# Day 02 — Finding and Interacting with Web Elements

## Topics Covered

### 1. Locator Strategies (The 8 Locators)
- `By.ID` — Find by element id attribute
- `By.NAME` — Find by name attribute
- `By.CLASS_NAME` — Find by CSS class name
- `By.TAG_NAME` — Find by HTML tag name
- `By.LINK_TEXT` — Find anchor by exact link text
- `By.PARTIAL_LINK_TEXT` — Find anchor by partial text
- `By.CSS_SELECTOR` — Find by CSS selector (powerful & fast)
- `By.XPATH` — Find by XPath expression (most flexible)

### 2. Finding Single vs Multiple Elements
- `driver.find_element(By.X, value)` — Returns first matching element
- `driver.find_elements(By.X, value)` — Returns list of all matching elements

### 3. Basic Element Interactions
- `.click()` — Click an element
- `.send_keys("text")` — Type into an input field
- `.clear()` — Clear a text field
- `.submit()` — Submit a form
- `.text` — Get visible text
- `.get_attribute("attr")` — Get attribute value
- `.is_displayed()` / `.is_enabled()` / `.is_selected()`

### 4. Working with Forms
- Text inputs, passwords
- Login form automation
- Registration form automation

### 5. CSS Selectors Deep Dive
- `#id`, `.class`, `tag`
- `tag.class`, `tag#id`
- `parent > child`, `parent child`
- `[attribute=value]`, `[attribute^=value]`, `[attribute$=value]`

### 6. XPath Deep Dive
- Absolute vs Relative XPath
- `//tag[@attribute='value']`
- `//tag[contains(@attr, 'value')]`
- `//tag[text()='value']`
- Axes: `parent::`, `child::`, `following-sibling::`, `preceding-sibling::`

---

## Demo Credentials
- **URL:** http://localhost:5000
- **Username:** `testuser` | **Password:** `password123`

---

## Homework

See the `Homework/` folder:

1. **Exercise 1:** Find elements on the home page using all 8 locator strategies.
2. **Exercise 2:** Automate the login form with valid and invalid credentials.
3. **Exercise 3:** Complete the partial code for extracting product data.
4. **Exercise 4:** Use CSS selectors to find specific elements.
5. **Exercise 5 (Challenge):** Automate the full registration flow and verify success.
