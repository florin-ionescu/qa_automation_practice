

def test_valid_login(page):
    page.goto("https://example.com")

    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("secret")

    page.get_by_role("button", name="Login").click()