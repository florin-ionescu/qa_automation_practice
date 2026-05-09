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

    # Get the URL
    print("Docs:", page.url)

    browser.close()