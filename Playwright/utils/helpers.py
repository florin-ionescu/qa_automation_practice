# It's a file where you store reusable utility functions that help your tests.
# Instead of rewriting the same code repeatedly, you place it in helpers.py.

def take_screenshot(page, name):
    page.screenshot(path=f"screenshots/{name}.png")

