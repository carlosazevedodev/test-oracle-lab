def is_adult(age: int) -> bool:
    """
    Requirement:
    A user is considered an adult only if age is 18 or older.
    """

    # Buggy implementation on purpose:
    # This passes weak tests but violates the real requirement.
    return age >= 16


def is_adult_fixed(age: int) -> bool:
    """
    Correct implementation based on the actual requirement.
    """

    return age >= 18
