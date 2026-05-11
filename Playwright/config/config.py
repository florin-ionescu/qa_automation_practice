"""
Config is a file used to store configuration values for your automation framework.
Instead of hardcoding values everywhere, you keep them in one place.
Without config: repeated values, harder maintenance, bad for multiple environments
"""
base_url = "https://example.com"

username = "username"
password = "test123"

BROWSER = "chromium"
TIMEOUT = 30000
HEADLESS = False


# The above code can be called by importing it. You keep this one and create another .py file for your test

