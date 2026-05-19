import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10,5, 15),
    (0, 7, 7),
])

def test_sum(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize("word, expected_length", [
    ("cat", 3),
    ("python", 6),
    ("automation", 10),
])

def test_length(word, expected_length):
    assert len(word) == expected_length


@pytest.mark.parametrize("number", [2, 4, 6, 8])
def test_even_numbers(number):
    assert number % 2 == 0