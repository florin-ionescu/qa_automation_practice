from helpers import take_screenshot

def test_login(page):
    page.goto("https://www.google.com")
    take_screenshot(page, "google_home")
    login(page, "TEST_USER", "Test123")

# Screenshot Helper
def take_screeshot(page, name):
    page.screenshot(path=f"screenshots/{name}.png")

# Login Helpers - Instead of repeating login steps everywhere.
def login(page, username, password):
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
