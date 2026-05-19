
"""
self.assertEqual(actual, expected)      # actual == expected
self.assertNotEqual(actual, expected)   # actual != expected
self.assertTrue(value)                  # value is True
self.assertFalse(value)                 # value is False
self.assertIsNone(value)                # value is None
self.assertIsNotNone(value)             # value is not None
self.assertIn(item, list_or_text)       # item exists inside something
self.assertNotIn(item, list_or_text)    # item does not exist
self.assertGreater(a, b)                # a > b
self.assertLess(a, b)                   # a < b
"""

def test_string_equal():
    name = "Florin"
    assert name == "Florin"

def test_string_contains():
    message = "Welcome to Python testing"
    assert "Python" in message

def test_string_startswith():
    url = "https://example.com"
    assert url.startswith("https")

def test_string_endswith():
    filename = "report.pdf"
    assert filename.endswith(".pdf")

def test_string_lowercase():
    text = "HELLO"
    assert text.lower() == "hello"

def test_string_strip():
    text = "   Python   "
    assert text.strip() == "Python"