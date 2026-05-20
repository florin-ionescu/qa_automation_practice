
def test_list_length():
    fruits = ["apple", "banana", "orange"]
    assert len(fruits) == 3
    assert fruits[0] == "apple"

def test_item_in_list():
    fruits = ["apple", "banana", "orange"]
    assert "banana" in fruits

def test_item_not_in_list():
    fruits = ["apple", "banana", "orange"]
    assert "kiwi" not in fruits

def test_first_item_in_list():
    fruits = ["apple", "banana", "orange"]
    assert fruits[0] == "apple"

def test_last_item_in_list():
    fruits = ["apple", "banana", "orange"]
    assert fruits[-1] == "orange"

def test_append():
    fruits = ["apple", "banana", "orange"]
    fruits.append("kiwi")
    assert fruits == ["apple", "banana", "orange", "kiwi"]

def test_remove_item():
    fruits = ["apple", "banana", "orange"]
    fruits.remove("banana")

    assert fruits == ["apple", "orange"]

def test_list_sum():
    numbers = [1, 2, 3, 4]

    assert sum(numbers) == 10

def test_list_count():
    numbers = [1, 2, 2, 3]
    assert numbers.count(2) == 2