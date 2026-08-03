from playwright.sync_api import Page, expect
import uuid

# =========================================================
# UI HELPERS
# =========================================================

# ---------------------------------------------------------
# Register a new user through the real frontend
# ---------------------------------------------------------
def ui_register(page: Page, username: str, password: str):
    page.goto("http://127.0.0.1:8000/register")

    page.fill("#first_name", "Test")
    page.fill("#last_name", "User")
    page.fill("#email", f"{username}@example.com")
    page.fill("#username", username)
    page.fill("#password", password)
    page.fill("#confirm_password", password)

    page.click("#register-btn")

    # Allow JS to validate, send POST, show success, redirect
    page.wait_for_timeout(3000)


# ---------------------------------------------------------
# Log in using your real JavaScript login flow
# ---------------------------------------------------------
def ui_login(page: Page, username: str, password: str):
    page.goto("http://127.0.0.1:8000/login")

    page.fill("#username", username)
    page.fill("#password", password)

    # Triggers your JS login handler (fetch → JWT → redirect)
    page.click("form#loginForm button[type='submit']")

    # Allow JS to run login flow
    page.wait_for_timeout(3000)

    # Wait for redirect to dashboard
    page.wait_for_url("http://127.0.0.1:8000/dashboard", timeout=5000)

    page.screenshot(path="debug_dashboard.png")


# ---------------------------------------------------------
# Perform ANY arithmetic operation on the dashboard
# ---------------------------------------------------------
def ui_operation(page: Page, operation: str, *numbers: str):
    # Wait for calculator UI
    page.wait_for_selector("#calcType", timeout=5000)

    # Select operation (addition, subtraction, etc.)
    page.select_option("#calcType", operation)

    # Fill comma-separated inputs
    page.fill("#calcInputs", ", ".join(numbers))

    # Submit calculation
    page.click("form#calculationForm button[type='submit']")

    # Wait for success alert
    page.wait_for_selector("#successAlert", timeout=5000)
    result_alert = page.locator("#successAlert")

    expect(result_alert).to_be_visible()

    # Screenshot after result
    page.screenshot(path=f"debug_{operation}_result.png")

    return result_alert.inner_text()


# =========================================================
# E2E TESTS — ARITHMETIC OPERATIONS
# =========================================================

# ---------------------------------------------------------
# Modulus with two numbers
# ---------------------------------------------------------
def test_e2e_modulus_two_numbers(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 100 % 30 = 10
    result = ui_operation(page, "modulus", "100", "30")
    assert "10" in result


# ---------------------------------------------------------
# Modulus with three numbers
# ---------------------------------------------------------
def test_e2e_modulus_three_numbers(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 100 % 30 % 4 = 2
    result = ui_operation(page, "modulus", "100", "30", "4")
    assert "2" in result


# ---------------------------------------------------------
# Addition
# ---------------------------------------------------------
def test_e2e_addition(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 10 + 20 + 30 = 60
    result = ui_operation(page, "addition", "10", "20", "30")
    assert "60" in result


# ---------------------------------------------------------
# Subtraction
# ---------------------------------------------------------
def test_e2e_subtraction(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 100 - 30 - 20 = 50
    result = ui_operation(page, "subtraction", "100", "30", "20")
    assert "50" in result


# ---------------------------------------------------------
# Multiplication
# ---------------------------------------------------------
def test_e2e_multiplication(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 2 * 3 * 4 = 24
    result = ui_operation(page, "multiplication", "2", "3", "4")
    assert "24" in result


# ---------------------------------------------------------
# Division
# ---------------------------------------------------------
def test_e2e_division(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # 100 / 5 / 2 = 10
    result = ui_operation(page, "division", "100", "5", "2")
    assert "10" in result


# =========================================================
# E2E TESTS — UI VALIDATION
# =========================================================

# ---------------------------------------------------------
# Invalid input should trigger an error
# ---------------------------------------------------------
def test_e2e_invalid_input(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # Select operation
    page.wait_for_selector("#calcType")
    page.select_option("#calcType", "modulus")

    # Fill invalid input
    page.fill("#calcInputs", "abc, 10")

    # Submit form
    page.click("form#calculationForm button[type='submit']")

    # Wait for error alert to appear
    error_alert = page.locator("#errorAlert")
    expect(error_alert).to_be_visible(timeout=7000)

    # Optional: assert message text
    message = page.locator("#errorMessage").inner_text()
    assert message.strip() != ""



# ---------------------------------------------------------
# History table should update after a calculation
# ---------------------------------------------------------
def test_e2e_history_updates(page: Page):
    username = f"user_{uuid.uuid4()}"
    password = "Password123!"

    ui_register(page, username, password)
    ui_login(page, username, password)

    # Perform a calculation
    ui_operation(page, "modulus", "100", "30")

    # 1. Wait for loading row to disappear
    page.wait_for_selector("#loadingRow", state="detached", timeout=7000)

    # 2. Now wait for at least one REAL row
    rows = page.locator("#calculationsTable tr")
    expect(rows).to_have_count(1, timeout=7000)

    # 3. Validate row is visible
    expect(rows.first).to_be_visible()

    # Debug print
    print("History rows:", rows.all_inner_texts())


