
def test_user_name(user):
    assert user["username"] == "Florin"

def test_user_active(user):
    assert user["is_active"] is True

def test_login_data(login_data):
    assert login_data["username"] == "Florin"
    assert login_data["password"] == "password123"

def test_equal():
    assert True
def test_not_equal():
    assert False

def test_equal():
    assert 5 == 5

def test_true():
    is_logged_in = True
    assert is_logged_in

def test_false():
    has_error = False
    assert not has_error

def test_greater_than():
    assert 5>5

def test_less_than():
    assert 4<5

def test_in_text():
    message = "I am learning Python Testing now"
    assert "Python" in message

def test_not_in_text():
    message = "I am learning Python Testing now"
    assert "Java" not in message

def test_is_not_none():
    name = "Florin"
    assert name is not None
def test_none():
    x = None
    assert x is None
