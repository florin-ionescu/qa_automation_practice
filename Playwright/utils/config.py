"""
Config is a file used to store configuration values for your automation framework.
Instead of hardcoding values everywhere, you keep them in one place.
Without config: repeated values, harder maintenance, bad for multiple environments
"""
BASE_URL = "https://example.com"

USERNAME = "username"
PASSWORD = "test123"

BROWSER = "chromium"
TIMEOUT = 30000
HEADLESS = False


"""
Most QA frameworks use uppercase for config:
BASE_URL
USERNAME
PASSWORD
HEADLESS
TIMEOUT

Uppercase is just the cleaner professional convention for configs/constants.
"""

# The above code can be called by importing it. You keep this one and create another .py file for your test

