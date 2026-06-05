from src.validators import is_adult_fixed


def test_user_under_18_is_not_adult():
    assert is_adult_fixed(17) is False


def test_user_exactly_18_is_adult():
    assert is_adult_fixed(18) is True


def test_user_above_18_is_adult():
    assert is_adult_fixed(21) is True


def test_child_user_is_not_adult():
    assert is_adult_fixed(10) is False
