"""A locator in Playwright is an object that represents a way to find and interact with an element on a webpage.
Locator = a query used to find elements on the page
"""
button = page.get_by_role("button", name="Submit") #button is a locator it points to the Submit button

'''Locators priority:
get_by_role()
get_by_label()
get_by_text()
get_by_test_id()    
CSS/XPath only if needed'''

#get_by_role() Find by ARIA role + accessible name. // best for: buttons,links, inputs, accessible UI
page.get_by_role("button", name="Login")

#get_by_text  = Find by visible text.
page.get_by_text("Welcome")
page.get_by_text("Welcome", exact=True) # exact match

#get_by_label()  Find form controls by label text.
page.get_by_label("Email") #  <label>Email</label>

#get_by_placeholder() Find inputs by placeholder.
page.get_by_placeholder("Enter email")

#get_by_alt_text() Find images by alt text.
page.get_by_alt_text("Company logo")

#get_by_title() Find Elements ty title attribute
page.get_by_title("Close") #<button title="Close">

#get_by_test_id() - find using test IDs
page.get_by_test_id("submit-btn") # <button data-testid="submit-btn">

#locator() =  Generic CSS/XPath/custom locator.
page.locator(".card")  #CSS
page.locator("//button[text()='Save']") #XPath

'''Filtering locators + examples:
.filter()  page.get_by_role("listitem").filter(has_text="Product 2")
.nth()     page.locator(".item").nth(2)
.first     page.locator(".item").first
.last      page.locator(".item").last
'''

"""Useful Locator Methods"""
"""
locator.click()
locator.fill("hello")
locator.type("hello")
locator.check()
locator.select_option("US")
locator.hover()
locator.text_content()
expect(locator).to_be_visible()
expect(locator).to_have_text("Success")
"""

page.goto("https://example.com") # Open the Website>Opens the browser page>Navigates to the URL

#Find Username Field and Type get_by_label("Username") //
page.get_by_label("Username").fill("admin") #Finds an input associated with the label: <label>Username</label>
page.get_by_label("Password").fill("secret")

page.get_by_role("button", name="Login").click() #simulates a real mouse click

expect(page.get_by_text("Dashboard")).to_be_visible()