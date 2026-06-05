from src.validators import is_adult


def test_adult_user_returns_true():
    assert is_adult(20) is True


def test_child_user_returns_false():
    assert is_adult(10) is False
