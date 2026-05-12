# is usually a test file that verifies a website’s search functionality.
#example

# Used for assertions. Assertions verify expected behavior.
from playwright.sync_api import expect

# test_ prefix tells pytest this is a test. page is Playwright’s browser page fixture
def test_search_product(page):
    #open website
    page.goto("https://www.google.com")

    # Type into search box
    page.get_by_placeholder("Search").fill("Laptop")

    # Click search button
    page.get_by_role("button", name="Search").click()

    # Verify results appear
    expect(page.get_by_text("Laptop")).to_be_visible()