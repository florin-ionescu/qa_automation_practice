
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