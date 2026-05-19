from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch the browser
    browser = playwright.firefox.launch(headless=False)
    #create a new page
    page = browser.new_page()
    #visit playwright page
    url = "https://playwright.dev/"
    page.goto(url)

    #locate a link element with Docs text and click on it
    docs_button = page.get_by_role('link', name='Docs')
    docs_button.click()
    page.screenshot(path="./screenshot.png")

    # Get the URL
    print("Docs:", page.url)

    browser.close()


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    url = page.goto("https://bootswatch.com/cosmo/")

    page.get_by_role("button", name="Block button").highlight()
    input("Press Enter to close...")
