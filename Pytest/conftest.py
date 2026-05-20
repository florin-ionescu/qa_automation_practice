import pytest

@pytest.fixture
def fruits():
    return ['apple', 'banana', 'orange']

@pytest.fixture
def numbers():
    return [1, 2, 3]

@pytest.fixture
def user():
    return {
        'username': 'Florin',
        'role': 'QA Automation',
        "is_active": True
    }

@pytest.fixture
def login_data():
    return {
        "username": "Florin",
        "password": "password123"
    }

