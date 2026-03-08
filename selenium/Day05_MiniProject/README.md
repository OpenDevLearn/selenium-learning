# Day 05 — Mini Project: End-to-End Test Suite

## Topics Covered

### 1. Structuring Test Code
- Organizing tests into functions
- Test setup and teardown
- Reusable helper functions
- The Page Object Model (POM) pattern — intro

### 2. Page Object Model (POM)
- What is POM and why it matters
- Creating page classes
- Separating locators from test logic
- Making tests maintainable

### 3. Writing a Real Test Suite
- End-to-end test scenarios
- Data-driven testing concepts
- Test reporting (simple pass/fail output)

### 4. Best Practices
- Always use explicit waits (not `time.sleep()`)
- Use descriptive element locators (ID > CSS > XPath)
- Handle exceptions gracefully
- Take screenshots on failure
- Keep tests independent
- Use meaningful test names

### 5. Mini Project
Students will build a complete test suite covering:
- User registration and login
- Product browsing and filtering
- Shopping cart workflow
- Form submission and validation
- Dynamic content handling

---

## Session Code

The `Session/` folder contains:
- A complete Page Object Model implementation
- A full test suite using the POM
- Helper utilities

## Homework (Final Project)

See the `Homework/` folder:

1. **Exercise 1:** Extend the POM with a new page object for the tables page.
2. **Exercise 2:** Write 5 additional test cases for scenarios not covered in class.
3. **Exercise 3:** Add data-driven tests using multiple test data sets.
4. **Exercise 4 (Challenge):** Create a comprehensive test report showing all results.
