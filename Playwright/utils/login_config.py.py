# EXAMPLE #
import click
from playwright.sync_api import expect
import config  # It's the name of the file

def test_login():
    page.goto(config.BASE_URL)

    page.get_by_label("Username").fill(config.USERNAME)
    page.get_by_label("Password").fill(config.PASSWORD)

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Dashboard")).to_be_empty()